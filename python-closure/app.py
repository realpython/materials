import tkinter as tk

app = tk.Tk()
app.title("GUI App")
app.geometry("320x240")

label = tk.Label(app, font=("Helvetica", 16, "bold"))
label.pack()


def callback(text):
    def closure():
        label.config(text=text)

    return closure


button = tk.Button(
    app,
    text="Greet",
    command=callback("Hello, World!"),
)
button.pack()

app.mainloop()
