import getpass
import os


def verify_email(email):
    allowed_emails = [
        email.strip() for email in os.getenv("ALLOWED_EMAILS").split(",")
    ]
    return email in allowed_emails


def main():
    email = getpass.getpass("Enter your email address: ")
    if verify_email(email):
        print("Email is valid. You can proceed.")
    else:
        print("Incorrect email. Access denied.")


if __name__ == "__main__":
    main()
