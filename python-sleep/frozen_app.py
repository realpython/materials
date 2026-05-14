import tkinter
import time

DELAY = 3  # Sleep for 3 seconds


def on_click():
    time.sleep(DELAY)
    print("Done!")


root = tkinter.Tk()
root.geometry("400x400")
button = tkinter.Button(text="Click me!", command=on_click)
button.pack()

root.mainloop()
