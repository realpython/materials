from enum import Enum, auto


class Message(Enum):
    ACKNOWLEDGE = auto()
    CURRENT_TRACK = auto()
    FIRST_TRACK = auto()
    GRACEFUL_STOP = auto()
    NEXT_PAGE = auto()
    PAGE = auto()
    PAUSE = auto()
    PLAY = auto()
    PLAY_TRACK = auto()
    PREVIOUS_PAGE = auto()
