import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

FILE_TYPES = [("Text Files", "*.txt"), ("All Files", "*.*")]


root = tk.Tk()
root.title("Simple Text Editor")


def open_file():
    path = askopenfilename(filetypes=FILE_TYPES)
    if path:
        with open(path, mode="r", encoding="utf-8") as text_file:
            txt.delete("1.0", tk.END)
            txt.insert(tk.END, text_file.read())


def save_file():
    path = asksaveasfilename(defaultextension=".txt", filetypes=FILE_TYPES)
    if path:
        with open(path, mode="w", encoding="utf-8") as text_file:
            text_file.write(txt.get("1.0", tk.END))


frame = tk.Frame(root)
frame.pack(side=tk.LEFT, fill=tk.Y)

tk.Button(
    frame,
    text="Open",
    command=open_file,
).pack(fill=tk.X, padx=5, pady=5)
tk.Button(
    frame,
    text="Save As...",
    command=save_file,
).pack(fill=tk.X, padx=5, pady=5)

txt = tk.Text(root)
txt.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


root.mainloop()
