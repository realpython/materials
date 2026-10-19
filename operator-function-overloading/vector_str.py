class Vector:
    def __init__(self, x_comp, y_comp):
        self.x_comp = x_comp
        self.y_comp = y_comp

    def __str__(self):
        # By default, sign of +ve number is not displayed
        # Using `+`, sign is always displayed
        return f"{self.x_comp}i{self.y_comp:+}j"
