import time
from typing import Annotated
from pydantic import PositiveFloat, validate_call, Field, EmailStr


@validate_call
def send_invoice(
    client_name: Annotated[str, Field(min_length=1)],
    client_email: EmailStr,
    items_purchased: list[str],
    amount_owed: PositiveFloat,
) -> str:

    email_str = f"""
    Dear {client_name}, \n
    Thank you for choosing xyz inc! You
    owe ${amount_owed:,.2f} for the following items: \n
    {items_purchased}
    """

    print(f"Sending email to {client_email}...")
    time.sleep(2)

    return email_str


send_invoice(
    client_name="Andrew Jolawson",
    client_email="ajolawson@fakedomain.com",
    items_purchased=["pie", "cookie", "cake"],
    amount_owed=12303,
)

send_invoice(
    client_name="",
    client_email="ajolawsonfakedomain.com",
    items_purchased=["pie", "cookie", 17],
    amount_owed=0,
)
