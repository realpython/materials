from js import document
from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.models import GameState


class BrowserRenderer(Renderer):
    def render(self, game_state: GameState) -> None:
        for i, cell in enumerate(game_state.grid.cells):
            button = document.querySelector(f"[data-id='{i}'] text")
            button.classList.remove("win")
            button.innerHTML = "&nbsp;" if cell == " " else cell
        status = document.querySelector("#status")
        if game_state.game_over:
            document.querySelector("#replay").classList.remove("hidden")
            for select in document.querySelectorAll("select"):
                select.removeAttribute("disabled")
            if game_state.winner:
                status.innerHTML = f"{game_state.winner} wins \N{party popper}"
                for i in game_state.winning_cells:
                    button = document.querySelector(f"[data-id='{i}'] text")
                    button.classList.add("win")
            elif game_state.tie:
                status.innerHTML = "Tie \N{neutral face}"
        else:
            document.querySelector("#status").innerHTML = ""
