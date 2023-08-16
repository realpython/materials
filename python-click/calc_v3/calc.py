import click
import commands


@click.group()
def cli():
    pass


cli.add_command(commands.add)
cli.add_command(commands.sub)
cli.add_command(commands.mul)
cli.add_command(commands.div)


if __name__ == "__main__":
    cli()
