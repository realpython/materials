import os
from typing import Any
import numpy as np
from langchain.graphs import Neo4jGraph


def get_current_wait_times(
    hospital: str, validate_hospital: bool = True
) -> str | float:
    """Get the current wait time at a hospital"""

    if validate_hospital:
        graph = Neo4jGraph(
            url=os.getenv("NEO4J_URI"),
            username=os.getenv("NEO4J_USERNAME"),
            password=os.getenv("NEO4J_PASSWORD"),
        )

        current_hospitals = graph.query(
            """
            MATCH (h:Hospital)
            RETURN h.name AS hospital_name
            """
        )

        current_hospitals = [
            d["hospital_name"].lower() for d in current_hospitals
        ]

        if hospital.lower() not in current_hospitals:
            return f"Hospital '{hospital}' does not exist"

    return np.random.randint(low=0, high=600)


def find_most_available_hospital(dummy_input: Any) -> dict[str, float]:
    """Find the hospital with the shortest wait time"""

    graph = Neo4jGraph(
        url=os.getenv("NEO4J_URI"),
        username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"),
    )

    current_hospitals = graph.query(
        """
        MATCH (h:Hospital)
        RETURN h.name AS hospital_name
        """
    )

    current_hospitals = [d["hospital_name"].lower() for d in current_hospitals]

    current_wait_times = [
        get_current_wait_times(h, validate_hospital=False)
        for h in current_hospitals
    ]

    best_time_idx = np.argmin(current_wait_times)
    best_hospital = current_hospitals[best_time_idx]
    best_wait_time = current_wait_times[best_time_idx]

    return {best_hospital: best_wait_time}
