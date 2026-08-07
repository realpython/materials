import tkinter as tk

root = tk.Tk()

frame_a = tk.Frame(master=root)
frame_b = tk.Frame(master=root)

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

# Swap the order of `frame_a` and `frame_b`
frame_b.pack()
frame_a.pack()

root.mainloop()
