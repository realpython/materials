import click


@click.command()
@click.option(
    "--weekday",
    type=click.Choice(
        ["monday", "tuesday", "wednesday", "thursday", "friday"]
    ),
)
def cli(weekday):
    click.echo(f"Weekday: {weekday}")


if __name__ == "__main__":
    cli()
