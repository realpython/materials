import click


@click.command()
@click.argument(
    "files",
    nargs=-1,
    type=click.File(mode="r"),
)
def cli(files):
    for file in files:
        click.echo(file.read().rstrip())


if __name__ == "__main__":
    cli()
