from pathlib import Path

import click


@click.command()
@click.argument(
    "path",
    type=click.Path(
        exists=True,
        file_okay=False,
        readable=True,
        path_type=Path,
    ),
)
def cli(path):
    for entry in path.iterdir():
        click.echo(f"{entry.name:{len(entry.name) + 5}}", nl=False)

    click.echo()


if __name__ == "__main__":
    cli()
