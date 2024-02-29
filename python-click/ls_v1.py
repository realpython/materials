from pathlib import Path

import click


@click.command()
@click.argument("path")
def cli(path):
    target_dir = Path(path)
    if not target_dir.exists():
        click.echo("The target directory doesn't exist")
        raise SystemExit(1)

    for entry in target_dir.iterdir():
        click.echo(f"{entry.name:{len(entry.name) + 5}}", nl=False)

    click.echo()


if __name__ == "__main__":
    cli()
