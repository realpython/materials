import tkinter as tk

root = tk.Tk()
root.geometry("200x80")

counter = 0


def handle_click(event):
    global counter
    counter += 1
    label.config(text="Click Count: " + str(counter))


label = tk.Label(root, text="Click Count: 0")
label.pack()

button = tk.Button(text="Click me!")
button.pack()


button.bind("<Button-1>", handle_click)

root.mainloop()
