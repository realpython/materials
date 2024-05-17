class Article:
    def __init__(self, title, author, pub_date):
        self.title = title
        self.author = author
        self.pub_date = pub_date

    def __str__(self):
        return (
            f"Article: {self.title}\n"
            f"Author: {self.author}\n"
            f"Published: {self.pub_date}\n"
        )

    def __repr__(self):
        return (
            f"{type(self).__name__}("
            f"title={self.title}, "
            f"author={self.author}, "
            f"pub_date={self.pub_date})"
        )


if __name__ == "__main__":
    article = Article(
        title="String Interpolation in Python: Exploring Available Tools",
        author="Real Python",
        pub_date="2024-05-15",
    )

    print(f"{article!s}")
    print(f"{article!r}")
