import datetime


class Article:
    def __init__(self, title, author, pub_date=None):
        self.title = title
        self.author = author
        self.pub_date = self.update_pub_date(pub_date)

    def update_pub_date(self, pub_date=None):
        if pub_date is None:
            date = datetime.datetime.now()
        else:
            date = datetime.datetime.fromisoformat(pub_date)
        return date

    def compute_age(self):
        now = datetime.datetime.now()
        return now - self.pub_date
