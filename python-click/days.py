import click


@click.command()
@click.option(
    "--weekday",
    type=click.Choice(
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
    ),
)
def cli(weekday):
    click.echo(f"Weekday: {weekday}")


if __name__ == "__main__":
    cli()
