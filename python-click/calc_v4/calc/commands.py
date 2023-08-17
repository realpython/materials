import click


@click.command(help="Add two numbers.")
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def add(a, b):
    click.echo(a + b)


@click.command(help="Subtract two numbers.")
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def sub(a, b):
    click.echo(a - b)


@click.command(help="Multiply two numbers.")
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def mul(a, b):
    click.echo(a * b)


@click.command(help="Divide two numbers.")
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def div(a, b):
    click.echo(a / b)
