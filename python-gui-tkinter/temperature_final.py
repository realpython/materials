import tkinter as tk

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x70")
root.resizable(width=False, height=False)


def fahrenheit_to_celsius():
    fahrenheit = ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


ent_temperature = tk.Entry(master=root, width=10)
ent_temperature.grid(row=0, column=0, padx=6, pady=20)

tk.Label(master=root, text="\N{DEGREE FAHRENHEIT}").grid(
    row=0, column=1, padx=6, pady=20
)


tk.Button(
    master=root,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius,
).grid(row=0, column=2, padx=6, pady=20)

lbl_result = tk.Label(master=root, text="\N{DEGREE CELSIUS}")
lbl_result.grid(row=0, column=3, padx=6, pady=20)

root.mainloop()
