import tkinter as tk

root = tk.Tk()
root.geometry("200x80")

counter = 0


def handle_click():
    global counter
    counter += 1
    label.config(text="Click Count: " + str(counter))


label = tk.Label(root, text="Click Count: 0")
label.pack()

button = tk.Button(text="Click me!", command=handle_click)
button.pack()


root.mainloop()
