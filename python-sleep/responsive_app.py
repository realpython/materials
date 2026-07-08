import tkinter

DELAY = 3000  # The after() method takes milliseconds (3000 ms = 3 seconds)


def on_click():
    root.after(DELAY, lambda: print("Done!"))


root = tkinter.Tk()
root.geometry("400x400")
button = tkinter.Button(text="Click me!", command=on_click)
button.pack()

root.mainloop()
