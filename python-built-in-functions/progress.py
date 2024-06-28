def progress(percent=0, width=30):
    end = ""
    if percent == 100:
        end = "\n"
    left = width * percent // 100
    right = width - left
    print(
        "\r[",
        "#" * left,
        " " * right,
        "]",
        f" {percent:.0f}%",
        sep="",
        end=end,
        flush=True,
    )
