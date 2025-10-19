"""This module provides the RP To-Do CLI."""

from pathlib import Path
from typing import List, Optional

import typer
from rptodo import ERRORS, __app_name__, __version__, config, database, rptodo

app = typer.Typer()


@app.command()
def init(
    db_path: str = typer.Option(
        str(database.DEFAULT_DB_FILE_PATH),
        "--db-path",
        "-db",
        prompt="to-do database location?",
    ),
) -> None:
    """Initialize the to-do database."""
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[app_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    db_init_error = database.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
            f'Creating database failed with "{ERRORS[db_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(f"The to-do database is {db_path}", fg=typer.colors.GREEN)


def get_todoer() -> rptodo.Todoer:
    if config.CONFIG_FILE_PATH.exists():
        db_path = database.get_database_path(config.CONFIG_FILE_PATH)
    else:
        typer.secho(
            'Config file not found. Please, run "rptodo init"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    if db_path.exists():
        return rptodo.Todoer(db_path)
    else:
        typer.secho(
            'Database not found. Please, run "rptodo init"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)


@app.command()
def add(
    description: List[str] = typer.Argument(...),
    priority: int = typer.Option(2, "--priority", "-p", min=1, max=3),
) -> None:
    """Add a new to-do with a DESCRIPTION."""
    todoer = get_todoer()
    todo, error = todoer.add(description, priority)
    if error:
        typer.secho(
            f'Adding to-do failed with "{ERRORS[error]}"', fg=typer.colors.RED
        )
        raise typer.Exit(1)
    else:
        typer.secho(
            f"""to-do: "{todo["Description"]}" was added """
            f"""with priority: {priority}""",
            fg=typer.colors.GREEN,
        )


@app.command(name="list")
def list_all() -> None:
    """List all to-dos."""
    todoer = get_todoer()
    todo_list = todoer.get_todo_list()
    if len(todo_list) == 0:
        typer.secho(
            "There are no tasks in the to-do list yet", fg=typer.colors.RED
        )
        raise typer.Exit()
    typer.secho("\nto-do list:\n", fg=typer.colors.BLUE, bold=True)
    columns = (
        "ID.  ",
        "| Priority  ",
        "| Done  ",
        "| Description  ",
    )
    headers = "".join(columns)
    typer.secho(headers, fg=typer.colors.BLUE, bold=True)
    typer.secho("-" * len(headers), fg=typer.colors.BLUE)
    for id, todo in enumerate(todo_list, 1):
        desc, priority, done = todo.values()
        typer.secho(
            f"{id}{(len(columns[0]) - len(str(id))) * ' '}"
            f"| ({priority}){(len(columns[1]) - len(str(priority)) - 4) * ' '}"
            f"| {done}{(len(columns[2]) - len(str(done)) - 2) * ' '}"
            f"| {desc}",
            fg=typer.colors.BLUE,
        )
    typer.secho("-" * len(headers) + "\n", fg=typer.colors.BLUE)


@app.command(name="complete")
def set_done(todo_id: int = typer.Argument(...)) -> None:
    """Complete a to-do by setting it as done using its TODO_ID."""
    todoer = get_todoer()
    todo, error = todoer.set_done(todo_id)
    if error:
        typer.secho(
            f'Completing to-do # "{todo_id}" failed with "{ERRORS[error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(
            f"""to-do # {todo_id} "{todo["Description"]}" completed!""",
            fg=typer.colors.GREEN,
        )


@app.command()
def remove(
    todo_id: int = typer.Argument(...),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Force deletion without confirmation.",
    ),
) -> None:
    """Remove a to-do using its TODO_ID."""
    todoer = get_todoer()

    def _remove():
        todo, error = todoer.remove(todo_id)
        if error:
            typer.secho(
                f'Removing to-do # {todo_id} failed with "{ERRORS[error]}"',
                fg=typer.colors.RED,
            )
            raise typer.Exit(1)
        else:
            typer.secho(
                f"""to-do # {todo_id}: '{todo["Description"]}' was removed""",
                fg=typer.colors.GREEN,
            )

    if force:
        _remove()
    else:
        todo_list = todoer.get_todo_list()
        try:
            todo = todo_list[todo_id - 1]
        except IndexError:
            typer.secho("Invalid TODO_ID", fg=typer.colors.RED)
            raise typer.Exit(1)
        delete = typer.confirm(
            f"Delete to-do # {todo_id}: {todo['Description']}?"
        )
        if delete:
            _remove()
        else:
            typer.echo("Operation canceled")


@app.command(name="clear")
def remove_all(
    force: bool = typer.Option(
        ...,
        prompt="Delete all to-dos?",
        help="Force deletion without confirmation.",
    ),
) -> None:
    """Remove all to-dos."""
    todoer = get_todoer()
    if force:
        error = todoer.remove_all().error
        if error:
            typer.secho(
                f'Removing to-dos failed with "{ERRORS[error]}"',
                fg=typer.colors.RED,
            )
            raise typer.Exit(1)
        else:
            typer.secho("All to-dos were removed", fg=typer.colors.GREEN)
    else:
        typer.echo("Operation canceled")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
) -> None:
    return
