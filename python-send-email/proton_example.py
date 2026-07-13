from proton_mail_bridge_client import ProtonMailClient

with ProtonMailClient(
    email="your-email@proton.me",
    password="your-bridge-password",  # Bridge password, NOT account password
) as client:
    client.send_mail(
        to="you@proton.com",
        subject="Test",
        body="This is a test",
    )
