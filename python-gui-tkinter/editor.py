import tkinter as tk

root = tk.Tk()
root.title("Simple Text Editor")

frame = tk.Frame(root)
frame.pack(side=tk.LEFT, fill=tk.Y)

tk.Button(
    frame,
    text="Open",
).pack(fill=tk.X, padx=5, pady=5)
tk.Button(
    frame,
    text="Save As...",
).pack(fill=tk.X, padx=5, pady=5)

txt = tk.Text(root)
txt.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

root.mainloop()
