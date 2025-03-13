import tkinter as tk


def main():
    window = tk.Tk()
    button = tk.Button(window, text="Click", command=lambda: on_click(42))
    button.pack(padx=10, pady=10)
    window.mainloop()


def on_click(age):
    if age > 18:
        print("You're an adult.")
    else:
        print("You're a minor.")


if __name__ == "__main__":
    main()
