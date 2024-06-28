from typing import Protocol


class ContentCreator(Protocol):
    def create_content(self) -> str: ...


class Blogger(ContentCreator, Protocol):
    posts: list[str]

    def add_post(self, title: str, content: str) -> None: ...


class Vlogger(ContentCreator, Protocol):
    videos: list[str]

    def add_video(self, title: str, path: str) -> None: ...


class Blog:
    def __init__(self):
        self.blog_posts = []

    def create_content(self) -> str:
        return "Creating a post."

    def add_post(self, title: str, content: str) -> None:
        self.blog_posts.append(f"{title}: {content}")
        print(f"Post added: {title}")


class Vlog:
    def __init__(self):
        self.videos = []

    def create_content(self) -> str:
        return "Recording a video."

    def add_video(self, title: str, path: str) -> None:
        self.videos.append(f"{title}: {path}")
        print(f"Video added: {title}")


def produce_content(creator: ContentCreator):
    print(creator.create_content())


def add_post(blogger: Blogger, title: str, content: str):
    blogger.add_post(title, content)


def add_video(vlogger: Vlogger, title: str, path: str):
    vlogger.add_video(title, path)
