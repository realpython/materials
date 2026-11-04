import tkinter as tk

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x70")
root.resizable(width=False, height=False)


ent_temperature = tk.Entry(master=root, width=10)
ent_temperature.grid(row=0, column=0, padx=6, pady=20)

tk.Label(master=root, text="\N{DEGREE FAHRENHEIT}").grid(
    row=0, column=1, padx=6, pady=20
)


tk.Button(
    master=root,
    text="\N{RIGHTWARDS BLACK ARROW}",
).grid(row=0, column=2, padx=6, pady=20)

lbl_result = tk.Label(master=root, text="\N{DEGREE CELSIUS}")
lbl_result.grid(row=0, column=3, padx=6, pady=20)

root.mainloop()
