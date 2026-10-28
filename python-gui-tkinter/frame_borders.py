import tkinter as tk

EFFECTS = (
    tk.FLAT,
    tk.SUNKEN,
    tk.RAISED,
    tk.GROOVE,
    tk.RIDGE,
)

root = tk.Tk()

for effect in EFFECTS:
    frame = tk.Frame(master=root, relief=effect, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=effect)
    label.pack()

root.mainloop()
