import logging

from opentelemetry import trace

from fastapi import FastAPI

app = FastAPI()
tracer = trace.get_tracer(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def simulate_db_query(user_id: int):
    with tracer.start_as_current_span("db_query") as span:
        span.set_attribute("db.system", "postgresql")
        span.set_attribute("user.id", user_id)

        trace_id = format(span.get_span_context().trace_id, "032x")
        span_id = format(span.get_span_context().span_id, "016x")

        if user_id == 999:
            logger.error(
                "DB query failed for user %s. trace_id=%s, span_id=%s",
                user_id,
                trace_id,
                span_id,
            )
            raise ValueError("Database connection lost!")

        logger.info(
            "Executing DB query for user %s. trace_id=%s, span_id=%s",
            user_id,
            trace_id,
            span_id,
        )
        return {"name": "Demo User", "role": "admin"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    logger.info("Received request for user %s", user_id)
    try:
        data = simulate_db_query(user_id)
        return {"status": "success", "data": data}
    except ValueError:
        return {"status": "error", "message": "Failed to fetch user"}


@app.get("/")
def read_root():
    return {"message": "Hello, OpenTelemetry!"}
