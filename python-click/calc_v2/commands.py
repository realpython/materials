import click


@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def add(a, b):
    click.echo(a + b)


@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def sub(a, b):
    click.echo(a - b)


@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def mul(a, b):
    click.echo(a * b)


@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def div(a, b):
    click.echo(a / b)
