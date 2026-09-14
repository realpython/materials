import tkinter as tk

root = tk.Tk()
root.title("Address Entry Form")

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

field_labels = [
    "First Name:",
    "Last Name:",
    "Address Line 1:",
    "Address Line 2:",
    "City:",
    "State/Province:",
    "Postal Code:",
    "Country:",
]

for index, text in enumerate(field_labels):
    tk.Label(
        master=frm_form,
        text=text,
    ).grid(row=index, column=0, sticky="e")
    tk.Entry(
        master=frm_form,
        width=50,
    ).grid(row=index, column=1)

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

root.mainloop()
