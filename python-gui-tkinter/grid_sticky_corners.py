import tkinter as tk

root = tk.Tk()
root.columnconfigure(0, minsize=250)
root.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="ne")

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="sw")

root.mainloop()
