import tkinter as tk

root = tk.Tk()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    fg="red",
)
button.pack()

root.mainloop()
