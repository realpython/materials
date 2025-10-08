# Set a custom color theme in Python 3.14
try:
    from _colorize import ANSIColors, default_theme, set_theme
except ImportError:
    pass
else:
    custom_theme = default_theme.copy_with(
        syntax=default_theme.syntax.copy_with(
            prompt=ANSIColors.GREY,
            builtin="\x1b[38;2;189;147;249m",
            comment="\x1b[38;2;98;114;164m",
            definition="\x1b[38;2;139;233;253m",
            keyword="\x1b[38;2;255;121;198m",
            keyword_constant="\x1b[38;2;255;121;198m",
            soft_keyword="\x1b[38;2;255;121;198m",
            number="\x1b[38;2;189;147;249m",
            op="\x1b[38;2;249;152;204m",
            string="\x1b[38;2;241;250;140m",
        ),
        traceback=default_theme.traceback.copy_with(
            error_highlight=ANSIColors.BOLD_YELLOW,
            error_range=ANSIColors.YELLOW,
            filename=ANSIColors.BACKGROUND_RED,
            frame=ANSIColors.BACKGROUND_RED,
            line_no=ANSIColors.BACKGROUND_RED,
            message=ANSIColors.RED,
            type=ANSIColors.BOLD_RED,
        ),
    )
    set_theme(custom_theme)

# Set a custom shell prompt
import platform
import sys

version = platform.python_version()
sys.ps1 = f"{version} \N{SNAKE} "
sys.ps2 = "." * len(sys.ps1)
