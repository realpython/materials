import click


@click.command()
@click.option("--size", type=(click.INT, click.INT))
def cli(size):
    width, height = size
    click.echo(f"size: {size}")
    click.echo(f"{width} × {height}")


if __name__ == "__main__":
    cli()
