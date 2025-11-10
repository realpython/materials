from argparse import ArgumentParser
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from inspect import signature

type PlainCallback = Callable[[], None]
type ListCallback = Callable[[str], None]
type TaskCallback = Callable[[str, Iterable[str]], None]


@dataclass(frozen=True)
class Callbacks:
    add: TaskCallback
    remove: TaskCallback
    done: TaskCallback
    undo: TaskCallback
    rename: Callable[[str, str, str], None]
    show: ListCallback
    clear: ListCallback
    lists: PlainCallback
    export: PlainCallback

    @property
    def task_callbacks(self) -> tuple[TaskCallback, ...]:
        return (
            self.add,
            self.remove,
            self.done,
            self.undo,
        )

    @property
    def list_callbacks(self) -> tuple[ListCallback, ...]:
        return (
            self.show,
            self.clear,
        )

    @property
    def plain_callbacks(self) -> tuple[PlainCallback, ...]:
        return (
            self.lists,
            self.export,
        )


def process_cli(callbacks: Callbacks) -> None:
    parser = build_parser(callbacks)
    args = parser.parse_args()
    if args.command:
        args.callback(
            **{
                name: getattr(args, name)
                for name in signature(args.callback).parameters
                if hasattr(args, name)
            }
        )
    else:
        parser.print_help()


def build_parser(callbacks: Callbacks) -> ArgumentParser:
    parser = ArgumentParser(description="A command-line task manager")
    subparsers = parser.add_subparsers(title="commands", dest="command")

    for cb in callbacks.task_callbacks:
        subparser = subparsers.add_parser(cb.__name__, help=cb.__doc__)
        subparser.set_defaults(callback=cb)
        add_tasks_positional(subparser)
        add_list_option(subparser)

    # Rename
    subparser = subparsers.add_parser("rename", help=callbacks.rename.__doc__)
    subparser.add_argument("old", type=normalize, help="original task name")
    subparser.add_argument("new", type=normalize, help="new task name")
    subparser.set_defaults(callback=callbacks.rename)
    add_list_option(subparser)

    for cb in callbacks.list_callbacks:
        subparser = subparsers.add_parser(cb.__name__, help=cb.__doc__)
        subparser.set_defaults(callback=cb)
        add_list_option(subparser)

    for cb in callbacks.plain_callbacks:
        subparser = subparsers.add_parser(cb.__name__, help=cb.__doc__)
        subparser.set_defaults(callback=cb)

    return parser


def add_tasks_positional(parser: ArgumentParser) -> None:
    parser.add_argument(
        "tasks",
        nargs="+",
        type=normalize,
        help="one or more tasks (e.g., 'eggs', 'bacon')",
    )


def add_list_option(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-l",
        "--list",
        dest="list_name",
        metavar="name",
        help="optional name of the task list (e.g., 'shopping')",
        default="default",
        type=normalize,
    )


def normalize(name: str) -> str:
    return name.strip().title()
