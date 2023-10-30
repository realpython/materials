from article_v1 import Article


class Tutorial(Article):
    def update_pub_date(self, pub_date=None):
        date = super().update_pub_date(pub_date)
        return date.strftime("%Y-%m-%d")
