# hello_gui/__main__.py

import tkinter as tk
from importlib import resources
from tkinter import ttk


class Hello(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wm_title("Hello")
        images = resources.files("hello_gui.gui_resources")

        # Read image, store a reference to it, and set it as an icon
        with resources.as_file(images / "logo.png") as path:
            self._icon = tk.PhotoImage(file=path)
        self.iconphoto(True, self._icon)

        # Read image, create a button, and store a reference to the image
        with resources.as_file(images / "hand.png") as path:
            hand = tk.PhotoImage(file=path)
        button = ttk.Button(
            self,
            image=hand,
            text="Goodbye",
            command=self.quit,
            compound=tk.LEFT,  # Add the image to the left of the text
        )
        button._image = hand
        button.pack(side=tk.TOP, padx=10, pady=10)


if __name__ == "__main__":
    hello = Hello()
    hello.mainloop()
