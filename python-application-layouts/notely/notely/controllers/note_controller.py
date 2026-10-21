class NoteController:
    """Handle user input and keep the view and the model in sync."""

    def __init__(self, store, window):
        self.store = store
        self.window = window
        self.window.new_button.clicked.connect(self.new_note)
        self.window.save_button.clicked.connect(self.save_notes)
        self.window.notes_list.currentRowChanged.connect(self.show_note)
        self.window.editor.textChanged.connect(self.update_body)
        for note in self.store.notes:
            self.window.notes_list.addItem(note.title)

    def current_note(self):
        row = self.window.notes_list.currentRow()
        return self.store.notes[row] if row >= 0 else None

    def new_note(self):
        note = self.store.add(f"Note {len(self.store.notes) + 1}")
        self.window.notes_list.addItem(note.title)
        self.window.notes_list.setCurrentRow(len(self.store.notes) - 1)

    def show_note(self, row):
        note = self.current_note()
        self.window.editor.setPlainText(note.body if note else "")

    def update_body(self):
        note = self.current_note()
        if note is not None:
            note.body = self.window.editor.toPlainText()

    def save_notes(self):
        self.store.save()
