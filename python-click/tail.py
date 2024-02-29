from collections import deque

import click


@click.command()
@click.option("-n", "--lines", type=click.INT, default=10)
@click.argument(
    "file",
    type=click.File(mode="r"),
)
def cli(file, lines):
    for line in deque(file, maxlen=lines):
        click.echo(line, nl=False)


if __name__ == "__main__":
    cli()
