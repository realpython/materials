import tkinter as tk

root = tk.Tk()
root.geometry("200x80")


label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=20)

current_text = []


def handle_keypress(event):
    if event.char.isprintable():
        current_text.append(event.char)
    label.config(text="".join(current_text))


root.bind("<KeyPress>", handle_keypress)

root.mainloop()
