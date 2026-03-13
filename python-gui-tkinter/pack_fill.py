import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(master=root, height=100, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=root, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=root, height=25, bg="blue")
frame3.pack(fill=tk.X)

root.mainloop()
