import click


@click.command()
@click.argument("name", default="World")
@click.option("--upper", "casing", flag_value="upper")
@click.option("--lower", "casing", flag_value="lower")
def cli(name, casing):
    message = f"Hello, {name}!"
    if casing == "upper":
        message = message.upper()
    elif casing == "lower":
        message = message.lower()
    click.echo(message)


if __name__ == "__main__":
    cli()
