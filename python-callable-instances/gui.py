class MainWindow:
    def show(self):
        print("Showing the app's main window...")

    def __call__(self):
        self.show()


window = MainWindow()
window.show()  # Or just window()
