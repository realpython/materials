import click


@click.command()
@click.option("--profile", type=click.Tuple([str, int]))
def cli(profile):
    click.echo(f"Hello, {profile[0]}! You're {profile[1]} years old!")


if __name__ == "__main__":
    cli()
