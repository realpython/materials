"""Provide a text-based user interface for a Bandcamp music player."""

from bandcamp.app.player import Player

COLUMN_WIDTH = CW = 30


def interact():
    """Control the player through user interactions."""
    with Player() as player:
        while True:
            print("\nType: play [<track_number>] | tracks | more | exit")
            match input("> ").strip().lower().split():
                case ["play"]:
                    play(player)
                case ["play", track]:
                    try:
                        track_number = int(track)
                        play(player, track_number)
                    except ValueError:
                        print("Please provide a valid track number.")
                case ["tracks"]:
                    display_tracks(player)
                case ["more"]:
                    player.discover.load_more()
                    display_tracks(player)
                case ["exit"]:
                    print("Exiting the player...")
                    break
                case _:
                    print("Unknown command. Try again.")


def play(player, track_number=None):
    """Play a track and show info about the track."""
    player.play(track_number)
    print(player._current_track._get_track_info())


def display_tracks(player):
    """Display information about the currently playable tracks."""
    header = (
        f"{'#':<5} {'Album':<{CW}} " f"{'Artist':<{CW}} " f"{'Genre':<{CW}}"
    )
    print(header)
    print("-" * 100)
    for track_number, track in enumerate(
        player.discover.available_tracks, start=1
    ):
        album, artist, *genre = track.text.split("\n")
        album = _truncate(album, CW)
        artist = _truncate(artist, CW)
        genre = _truncate(genre[0], CW) if genre else ""
        print(
            f"{track_number:<5} {album:<{CW}} " f"{artist:<{CW}} {genre:<{CW}}"
        )


def _truncate(text, width):
    """Truncate track information."""
    return text[: width - 3] + "..." if len(text) > width else text
