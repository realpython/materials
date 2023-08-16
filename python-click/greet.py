import click


@click.command()
@click.option("--name", multiple=True)
def cli(name):
    for n in name:
        click.echo(f"Hello, {n}!")


if __name__ == "__main__":
    cli()
