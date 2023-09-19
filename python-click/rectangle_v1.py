import click


@click.command()
@click.option("--size", nargs=2, type=click.INT)
def cli(size):
    width, height = size
    click.echo(f"size: {size}")
    click.echo(f"{width} × {height}")


if __name__ == "__main__":
    cli()
