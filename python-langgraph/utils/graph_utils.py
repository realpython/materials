import random
import time

from chains.notice_extraction import NoticeEmailExtract
from pydantic import EmailStr
from utils.logging_config import LOGGER


def send_escalation_email(
    notice_email_extract: NoticeEmailExtract, escalation_emails: list[EmailStr]
) -> None:
    """Simulate sending escalation emails"""

    LOGGER.info("Sending escalation emails...")
    for email in escalation_emails:
        time.sleep(1)
        LOGGER.info(f"Escalation email sent to {email}")


def create_legal_ticket(
    current_follow_ups: dict[str, bool] | None,
    notice_email_extract: NoticeEmailExtract,
) -> str | None:
    """Simulate creating a legal ticket using your company's API."""
    LOGGER.info("Creating legal ticket for notice...")
    time.sleep(2)

    follow_ups = [
        None,
        """Does this message mention the states of Texas, Georgia, or
        New Jersey?""",
        "Did this notice involve an issue with FakeAirCo's HVAC system?",
    ]

    if current_follow_ups:
        follow_ups = [
            f for f in follow_ups if f not in current_follow_ups.keys()
        ]

    follow_up = random.choice(follow_ups)

    if not follow_up:
        LOGGER.info("Legal ticket created!")
        return follow_up

    LOGGER.info("Follow-up is required before creating this ticket")

    return follow_up
