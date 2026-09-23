import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(master=root, width=100, height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=root, width=50, height=50, bg="yellow")
frame2.pack()

frame3 = tk.Frame(master=root, width=25, height=25, bg="blue")
frame3.pack()

root.mainloop()
