import logging
import os

from neo4j import GraphDatabase
from retry import retry

HOSPITALS_CSV_PATH = os.getenv("HOSPITALS_CSV_PATH")
PAYERS_CSV_PATH = os.getenv("PAYERS_CSV_PATH")
PHYSICIANS_CSV_PATH = os.getenv("PHYSICIANS_CSV_PATH")
PATIENTS_CSV_PATH = os.getenv("PATIENTS_CSV_PATH")
VISITS_CSV_PATH = os.getenv("VISITS_CSV_PATH")
REVIEWS_CSV_PATH = os.getenv("REVIEWS_CSV_PATH")

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

LOGGER = logging.getLogger(__name__)

NODES = ["Hospital", "Payer", "Physician", "Patient", "Visit", "Review"]


def _set_uniqueness_constraints(tx, node):
    query = f"""CREATE CONSTRAINT IF NOT EXISTS FOR (n:{node})
        REQUIRE n.id IS UNIQUE;"""
    tx.run(query, {})


@retry(tries=100, delay=10)
def load_hospital_graph_from_csv() -> None:
    """Load structured hospital CSV data following
    a specific ontology into Neo4j"""

    driver = GraphDatabase.driver(
        NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
    )

    LOGGER.info("Setting uniqueness constraints on nodes")
    with driver.session(database="neo4j") as session:
        for node in NODES:
            session.execute_write(_set_uniqueness_constraints, node)

    LOGGER.info("Loading hospital nodes")
    with driver.session(database="neo4j") as session:
        query = f"""
        LOAD CSV WITH HEADERS
        FROM '{HOSPITALS_CSV_PATH}' AS hospitals
        MERGE (h:Hospital {{id: toInteger(hospitals.hospital_id)}})
        SET h.name = hospitals.hospital_name,
            h.state_name = hospitals.hospital_state;
        """
        session.run(query, {})

    LOGGER.info("Loading payer nodes")
    with driver.session(database="neo4j") as session:
        query = f"""
        LOAD CSV WITH HEADERS
        FROM '{PAYERS_CSV_PATH}' AS payers
        MERGE (p:Payer {{id: toInteger(payers.payer_id)}})
        SET p.name = payers.payer_name;
        """
        session.run(query, {})

    LOGGER.info("Loading physician nodes")
    with driver.session(database="neo4j") as session:
        query = f"""
        LOAD CSV WITH HEADERS
        FROM '{PHYSICIANS_CSV_PATH}' AS physicians
        MERGE (p:Physician {{id: toInteger(physicians.physician_id)}})
        SET p.name = physicians.physician_name,
            p.dob = physicians.physician_dob,
            p.grad_year = physicians.physician_grad_year,
            p.school = physicians.medical_school,
            p.salary = toFloat(physicians.salary);
        """
        session.run(query, {})

    LOGGER.info("Loading visit nodes")
    with driver.session(database="neo4j") as session:
        query = f"""
        LOAD CSV WITH HEADERS FROM '{VISITS_CSV_PATH}' AS visits
        MERGE (v:Visit {{id: toInteger(visits.visit_id)}})
        SET v.room_number = toInteger(visits.room_number),
            v.admission_type = visits.admission_type,
            v.admission_date = visits.date_of_admission,
            v.test_results = visits.test_results,
            v.status = visits.visit_status,
            v.chief_complaint = visits.chief_complaint,
            v.treatment_description = visits.treatment_description,
            v.diagnosis = visits.primary_diagnosis,
            v.discharge_date = visits.discharge_date;
         """
        session.run(query, {})

    LOGGER.info("Loading patient nodes")
    with driver.session(database="neo4j") as session:
        query = f"""
        LOAD CSV WITH HEADERS
        FROM '{PATIENTS_CSV_PATH}' AS patients
        MERGE (p:Patient {{id: toInteger(patients.patient_id)}})
        SET p.name = patients.patient_name,
            p.sex = patients.patient_sex,
            p.dob = patients.patient_dob,
            p.blood_type = patients.patient_blood_type;
        """
        session.run(query, {})

    LOGGER.info("Loading review nodes")
    with driver.session(database="neo4j") as session:
        query = f"""
        LOAD CSV WITH HEADERS
        FROM '{REVIEWS_CSV_PATH}' AS reviews
        MERGE (r:Review {{id: toInteger(reviews.review_id)}})
        SET r.text = reviews.review,
            r.patient_name = reviews.patient_name,
            r.physician_name = reviews.physician_name,
            r.hospital_name = reviews.hospital_name;
        """
        session.run(query, {})

    LOGGER.info("Loading 'AT' relationships")
    with driver.session(database="neo4j") as session:
        query = f"""
        LOAD CSV WITH HEADERS FROM '{VISITS_CSV_PATH}' AS row
        MATCH (source: `Visit` {{ `id`: toInteger(trim(row.`visit_id`)) }})
        MATCH (target: `Hospital` {{ `id`:
        toInteger(trim(row.`hospital_id`))}})
        MERGE (source)-[r: `AT`]->(target)
        """
        session.run(query, {})

    LOGGER.info("Loading 'WRITES' relationships")
    with driver.session(database="neo4j") as session:
        query = f"""
        LOAD CSV WITH HEADERS FROM '{REVIEWS_CSV_PATH}' AS reviews
            MATCH (v:Visit {{id: toInteger(reviews.visit_id)}})
            MATCH (r:Review {{id: toInteger(reviews.review_id)}})
            MERGE (v)-[writes:WRITES]->(r)
        """
        session.run(query, {})

    LOGGER.info("Loading 'TREATS' relationships")
    with driver.session(database="neo4j") as session:
        query = f"""
        LOAD CSV WITH HEADERS FROM '{VISITS_CSV_PATH}' AS visits
            MATCH (p:Physician {{id: toInteger(visits.physician_id)}})
            MATCH (v:Visit {{id: toInteger(visits.visit_id)}})
            MERGE (p)-[treats:TREATS]->(v)
        """
        session.run(query, {})

    LOGGER.info("Loading 'COVERED_BY' relationships")
    with driver.session(database="neo4j") as session:
        query = f"""
        LOAD CSV WITH HEADERS FROM '{VISITS_CSV_PATH}' AS visits
            MATCH (v:Visit {{id: toInteger(visits.visit_id)}})
            MATCH (p:Payer {{id: toInteger(visits.payer_id)}})
            MERGE (v)-[covered_by:COVERED_BY]->(p)
            SET covered_by.service_date = visits.discharge_date,
                covered_by.billing_amount = toFloat(visits.billing_amount)
        """
        session.run(query, {})

    LOGGER.info("Loading 'HAS' relationships")
    with driver.session(database="neo4j") as session:
        query = f"""
        LOAD CSV WITH HEADERS FROM '{VISITS_CSV_PATH}' AS visits
            MATCH (p:Patient {{id: toInteger(visits.patient_id)}})
            MATCH (v:Visit {{id: toInteger(visits.visit_id)}})
            MERGE (p)-[has:HAS]->(v)
        """
        session.run(query, {})

    LOGGER.info("Loading 'EMPLOYS' relationships")
    with driver.session(database="neo4j") as session:
        query = f"""
        LOAD CSV WITH HEADERS FROM '{VISITS_CSV_PATH}' AS visits
            MATCH (h:Hospital {{id: toInteger(visits.hospital_id)}})
            MATCH (p:Physician {{id: toInteger(visits.physician_id)}})
            MERGE (h)-[employs:EMPLOYS]->(p)
        """
        session.run(query, {})


if __name__ == "__main__":
    load_hospital_graph_from_csv()
