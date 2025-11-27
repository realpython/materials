from rich.console import Console, Group
from rich.panel import Panel

from todolist.status import TaskListStatus

console = Console()


def render_short(status: TaskListStatus) -> None:
    if len(status) == 0:
        return
    console.print(f"{status.name} ({len(status.done)}/{len(status)})")


def render_long(status: TaskListStatus) -> None:
    if len(status) == 0:
        return

    lines = []
    if status.pending:
        lines.append("[b]Pending:[/]")
        lines.extend([f"☐ {name}" for name in status.pending])

    if status.done:
        if status.pending:
            lines.append("")
        lines.append("[b]Completed:[/]")
        lines.extend([f"[dim]🗹 [strike]{name}[/]" for name in status.done])

    panel = Panel(
        Group(*lines), title=status.name, width=60, border_style="bold"
    )
    console.print(panel)
