class Logger:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, message):
        with open(self.filename, mode="a", encoding="utf-8") as log_file:
            log_file.write(message + "\n")
