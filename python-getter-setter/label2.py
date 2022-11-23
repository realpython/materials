class Label:
    def __init__(self, text, font):
        self.set_text(text)
        self.font = font

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value.upper()  # Attached behavior
