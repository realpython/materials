from asyncio.queues import Queue

from js import document
from players import BrowserPlayer
from pyodide import create_proxy
from renderers import BrowserRenderer
from tic_tac_toe.game.engine_async import AsyncTicTacToe
from tic_tac_toe.game.players_async import (
    AsyncMinimaxComputerPlayer,
    AsyncRandomComputerPlayer,
)
from tic_tac_toe.logic.models import Mark

events = Queue()


async def main() -> None:

    player_x = document.querySelector("#playerX").value
    player_o = document.querySelector("#playerO").value

    if player_x == "random":
        player1 = AsyncRandomComputerPlayer(Mark("X"))
    elif player_x == "minimax":
        player1 = AsyncMinimaxComputerPlayer(Mark("X"))
    else:
        player1 = BrowserPlayer(Mark("X"), events)

    if player_o == "random":
        player2 = AsyncRandomComputerPlayer(Mark("O"))
    elif player_o == "minimax":
        player2 = AsyncMinimaxComputerPlayer(Mark("O"))
    else:
        player2 = BrowserPlayer(Mark("O"), events)

    await AsyncTicTacToe(player1, player2, BrowserRenderer()).play(
        starting_mark=Mark("X")
    )


def on_button_clicked(event) -> None:
    event.preventDefault()
    clicked_button = event.currentTarget
    if clicked_button.innerHTML != " ":
        events.put_nowait(int(clicked_button.dataset.id))


for cell in document.querySelectorAll("[data-id]"):
    cell.addEventListener("click", create_proxy(on_button_clicked))

button = document.querySelector("#replay")


async def on_replay(_=None) -> None:
    for select in document.querySelectorAll("select"):
        select.setAttribute("disabled", "")
    button.classList.add("hidden")
    await main()


button.addEventListener("click", create_proxy(on_replay))

on_replay()
