# Avoid this:
# class Article:
#     def __init__(self, title, body, tags, db):
#         self.title = title
#         self.body = body
#         self.tags = tags or []
#         self.db = db
#         self.slug = None
#         self.published = False

#     def publish(self):
#         if self.slug is None:
#             self.slug = "-".join(self.title.lower().split())

#         self.db.save_article(
#             title=self.title,
#             body=self.body,
#             tags=self.tags,
#             slug=self.slug,
#         )

#         self.published = True


# Favor this:
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Article:
    title: str
    body: str
    tags: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    published_at: datetime | None = None

    @property
    def is_published(self) -> bool:
        return self.published_at is not None

    @property
    def slug(self) -> str:
        return "-".join(self.title.lower().split())

    def __str__(self) -> str:
        status = "published" if self.is_published else "draft"
        return f"{self.title} [{status}]"


class Publisher:
    def __init__(self, db):
        self._db = db

    def publish(self, article: Article) -> None:
        if article.is_published:
            return
        article.published_at = datetime.utcnow()
        self._db.save(article)
