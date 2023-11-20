import time

from rich.progress import Progress

with Progress() as progress:
    task1 = progress.add_task("[red]Fribbulating...[/]", total=1000)
    task2 = progress.add_task("[green]Wobbulizing...[/]", total=1000)
    task3 = progress.add_task("[cyan]Fandangling...[/]", total=1000)
    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.9)
        time.sleep(0.01)
