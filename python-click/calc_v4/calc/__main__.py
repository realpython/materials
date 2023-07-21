import click

from . import commands


@click.group()
def cli():
    pass


cli.add_command(commands.add)
cli.add_command(commands.sub)
cli.add_command(commands.mul)
cli.add_command(commands.div)
