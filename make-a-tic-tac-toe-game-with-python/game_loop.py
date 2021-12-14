import PySimpleGUI as sg


def main():
    window = sg.Window("Tic-Tac-Toe", layout=[[]], margins=(100, 50))

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == "__main__":
    main()
