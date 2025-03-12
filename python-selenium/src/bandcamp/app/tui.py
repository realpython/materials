from bandcamp.app.player import Player


class TUI:
    """Provides a text-based user interface for a Bandcamp music player."""

    COLUMN_WIDTH = CW = 30
    MAX_TRACKS = 120  # Twice the number of tracks that fit in the viewport.

    def interact(self):
        """Controls the player through user interactions."""
        with Player() as player:
            while True:
                print(
                    "\nType: [play <track number>], [pause], [tracks], [more], [exit]"
                )
                command = input("> ").strip().lower()

                if command.startswith("play"):
                    try:
                        track_number = int(command.split()[1])
                        self.play(player, track_number)
                    except IndexError:  # Play first track.
                        self.play(player)
                    except ValueError:
                        print("Please provide a valid track number.")
                elif command == "pause":
                    self.pause(player)
                elif command == "tracks":
                    self.tracks(player)
                elif command == "more":
                    # A higher number of tracks can't be clicked without scrolling.
                    if len(player.tracklist.available_tracks) >= self.MAX_TRACKS:
                        print("Can't load more tracks. Pick one from the track list.")
                    else:
                        player.tracklist.load_more()
                        self.tracks(player)
                elif command == "exit":
                    print("Exiting the player...")
                    break
                else:
                    print("Unknown command. Try again.")

    def play(self, player, track_number=None):
        """Plays a track and shows info about the track."""
        player.play(track_number)
        print(player._current_track._get_track_info())

    def pause(self, player):
        """Pauses the current track."""
        player.pause()

    def tracks(self, player):
        """Displays information about the currently playable tracks."""
        header = (
            f"{'#':<5} {'Album':<{self.CW}} {'Artist':<{self.CW}} {'Genre':<{self.CW}}"
        )
        print(header)
        print("-" * 100)
        for track_number, track in enumerate(
            player.tracklist.available_tracks, start=1
        ):
            if track.text:
                album, artist, *genre = track.text.split("\n")
                album = self._truncate(album, self.CW)
                artist = self._truncate(artist, self.CW)
                genre = self._truncate(genre[0], self.CW) if genre else ""
                print(
                    f"{track_number:<5} {album:<{self.CW}} "
                    f"{artist:<{self.CW}} {genre:<{self.CW}}"
                )

    @staticmethod
    def _truncate(text, width):
        """Truncates track information."""
        return text[: width - 3] + "..." if len(text) > width else text
