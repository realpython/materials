import tkinter as tk

root = tk.Tk()

greeting = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10,
)
greeting.pack()

root.mainloop()
