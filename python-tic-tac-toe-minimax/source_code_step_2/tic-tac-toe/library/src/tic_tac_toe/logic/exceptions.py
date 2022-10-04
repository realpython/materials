# tic_tac_toe/logic/exceptions.py

class InvalidGameState(Exception):
    """Raised when the game state is invalid."""


class InvalidMove(Exception):
    """Raised when the move is invalid."""
