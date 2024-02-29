import click


@click.command("hello")
@click.version_option("0.1.0", prog_name="hello")
def hello():
    click.echo("Hello, World!")


if __name__ == "__main__":
    hello()
