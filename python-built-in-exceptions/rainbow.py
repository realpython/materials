COLORS = {
    "Red": {"Hex": "#FF0000", "RGB": (255, 0, 0)},
    "Orange": {"Hex": "#FF7F00", "RGB": (255, 127, 0)},
    "Yellow": {"Hex": "#FFFF00", "RGB": (255, 255, 0)},
    "Green": {"Hex": "#00FF00", "RGB": (0, 255, 0)},
    "Blue": {"Hex": "#0000FF", "RGB": (0, 0, 255)},
    "Indigo": {"Hex": "#4B0082", "RGB": (75, 0, 130)},
    "Violet": {"Hex": "#8B00FF", "RGB": (139, 0, 255)},
}


class RainbowColor:
    def __init__(self, name="Red"):
        name = name.title()
        if name not in COLORS:
            raise ValueError(f"{name} is not a valid rainbow color")
        self.name = name

    def as_hex(self):
        return COLORS[self.name]["Hex"]

    def as_rgb(self):
        return COLORS[self.name]["RGB"]
