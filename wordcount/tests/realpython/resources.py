from abc import ABC, abstractmethod
from dataclasses import dataclass
from inspect import getmembers, isclass, isfunction
from typing import Callable


@dataclass(unsafe_hash=True)
class ExternalResource:
    url: str
    title: str

    @property
    def title_pretty(self):
        return self.title

    def __str__(self) -> str:
        return f"[{self.title_pretty}]({self.url})"


@dataclass(unsafe_hash=True)
class Resource(ABC):
    slug: str
    title: str | None = None

    @property
    def slug_clean(self) -> str:
        return self.slug.strip("/")

    @property
    def title_pretty(self) -> str:
        if self.title is None:
            return self.slug_clean.replace("-", " ").title()
        else:
            return self.title

    @property
    @abstractmethod
    def url(self) -> str:
        pass

    def __str__(self) -> str:
        return f"[{self.title_pretty}]({self.url})"


@dataclass(unsafe_hash=True)
class Tutorial(Resource):
    section_id: str | None = None

    @property
    def title_pretty(self) -> str:
        if self.section_id and not self.title:
            return self.section.replace("-", " ").title()
        else:
            return super().title_pretty

    @property
    def url(self) -> str:
        if self.section_id:
            return f"https://realpython.com/{self.slug_clean}/#{self.section}"
        else:
            return f"https://realpython.com/{self.slug_clean}/"

    @property
    def section(self):
        return self.section_id.lstrip("#")


class Course(Resource):
    @property
    def url(self) -> str:
        return f"https://realpython.com/courses/{self.slug_clean}/"


class LearningPath(Resource):
    @property
    def url(self) -> str:
        return f"https://realpython.com/learning-paths/{self.slug_clean}/"


class Podcast(Resource):
    @property
    def url(self) -> str:
        return f"https://realpython.com/podcasts/rpp/{self.slug_clean}/"

    def __str__(self) -> str:
        episode = f"Episode {self.slug_clean}"
        if self.title:
            return f"[{episode}: {self.title_pretty}]({self.url})"
        else:
            return f"[{episode}]({self.url})"


def tutorial(
    slug: str, title: str | None = None, section: str | None = None
) -> Callable:
    return _associate(Tutorial, slug, title, section)


def course(slug: str, title: str | None = None) -> Callable:
    return _associate(Course, slug, title)


def learning_path(slug: str, title: str | None = None) -> Callable:
    return _associate(LearningPath, slug, title)


def podcast(slug: str, title: str | None = None) -> Callable:
    return _associate(Podcast, slug, title)


def external(url: str, title: str) -> Callable:
    return _associate(ExternalResource, url, title)


def _associate(resource: type, *args) -> Callable:
    def decorator(obj: type | Callable) -> type | Callable:
        match obj:
            case cls if isclass(obj):
                for name, function in getmembers(cls, isfunction):
                    if name.startswith("test"):
                        setattr(cls, name, decorator(function))
            case test_function if isfunction(obj):
                if not hasattr(test_function, "resources"):
                    test_function.resources = set()
                test_function.resources.add(resource(*args))
        return obj

    return decorator
