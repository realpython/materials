import json
import urllib.request
from dataclasses import dataclass

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel


@dataclass
class Comment:
    when: str
    body: str
    url: str
    user: str
    user_url: str
    issue_title: str

    @property
    def footer(self):
        return (
            f"Comment by [{self.user}]({self.user_url})"
            f" on [{self.when}]({self.url})"
        )

    def render(self):
        return Panel(
            Markdown(f"{self.body}\n\n---\n_{self.footer}_"),
            title=self.issue_title,
            padding=1,
        )


def fetch_github_events(org, repo):
    url = f"https://api.github.com/repos/{org}/{repo}/events"
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())


def filter_comments(events):
    for event in events:
        match event:
            case {
                "type": "IssueCommentEvent",
                "created_at": when,
                "actor": {
                    "display_login": user,
                },
                "payload": {
                    "action": "created",
                    "issue": {
                        "state": "open",
                        "title": issue_title,
                    },
                    "comment": {
                        "body": body,
                        "html_url": url,
                        "user": {
                            "html_url": user_url,
                        },
                    },
                },
            }:
                yield Comment(when, body, url, user, user_url, issue_title)


def main():
    console = Console()
    events = fetch_github_events("python", "cpython")
    for comment in filter_comments(events):
        console.clear()
        console.print(comment.render())
        console.input("\nPress [b]ENTER[/b] for the next comment...")


if __name__ == "__main__":
    main()
