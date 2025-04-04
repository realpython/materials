from bandcamp.app.player import Player

COLUMN_WIDTH = CW = 30
MAX_TRACKS = 100  # Allows to load more tracks once.


def interact():
    """Control the player through user interactions."""
    with Player() as player:
        while True:
            print(
                "\nType: play [<track number>] | pause | tracks | more | exit"
            )
            match input("> ").strip().lower().split():
                case ["play"]:
                    play(player)
                case ["play", track]:
                    try:
                        track_number = int(track)
                        play(player, track_number)
                    except ValueError:
                        print("Please provide a valid track number.")
                case ["pause"]:
                    pause(player)
                case ["tracks"]:
                    display_tracks(player)
                case ["more"] if (
                    len(player.tracklist.available_tracks) >= MAX_TRACKS
                ):
                    print(
                        "Can't load more tracks. Pick one from the track list."
                    )
                case ["more"]:
                    player.tracklist.load_more()
                    display_tracks(player)
                case ["exit"]:
                    print("Exiting the player...")
                    break
                case _:
                    print("Unknown command. Try again.")


def play(player, track_number=None):
    """Play a track and show info about the track."""
    try:
        player.play(track_number)
        print(player._current_track._get_track_info())
    except IndexError:
        print(
            "Please provide a valid track number. "
            "You can list available tracks with `tracks`."
        )


def pause(player):
    """Pause the current track."""
    player.pause()


def display_tracks(player):
    """Display information about the currently playable tracks."""
    header = f"{'#':<5} {'Album':<{CW}} {'Artist':<{CW}} {'Genre':<{CW}}"
    print(header)
    print("-" * 80)
    for track_number, track_element in enumerate(
        player.tracklist.available_tracks, start=1
    ):
        track = track_element._get_track_info()
        album = _truncate(track.album, CW)
        artist = _truncate(track.artist, CW)
        genre = _truncate(track.genre, CW)
        print(f"{track_number:<5} {album:<{CW}} {artist:<{CW}} {genre:<{CW}}")


def _truncate(text, width):
    """Truncate track information."""
    return text[: width - 3] + "..." if len(text) > width else text
