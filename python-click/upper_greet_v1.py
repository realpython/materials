import click


@click.command()
@click.argument("name", default="World")
@click.option("--upper/--no-upper", default=False)
def cli(name, upper):
    message = f"Hello, {name}!"
    if upper:
        message = message.upper()
    click.echo(message)


if __name__ == "__main__":
    cli()
