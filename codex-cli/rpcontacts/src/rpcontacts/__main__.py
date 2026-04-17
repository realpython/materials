from rpcontacts.database import Database
from rpcontacts.tui import ContactsApp


def main():
    app = ContactsApp(db=Database())
    app.run()


if __name__ == "__main__":
    main()
