from bandcamp.app.tui import TUI


def main():
    """Provides the main entry point for the app."""
    tui = TUI()
    tui.interact()


if __name__ == "__main__":
    main()
