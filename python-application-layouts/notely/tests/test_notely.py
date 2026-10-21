from notely.app import create_main_window
from notely.models import NoteStore


def test_store_round_trip(tmp_path):
    path = tmp_path / "notes.json"
    store = NoteStore(path)
    store.add("Groceries").body = "Eggs"
    store.save()
    assert NoteStore(path).notes[0].body == "Eggs"


def test_new_note_and_save(qapp, tmp_path):
    path = tmp_path / "notes.json"
    window = create_main_window(path)
    window.new_button.click()
    window.editor.setPlainText("Buy milk")
    window.save_button.click()
    assert window.notes_list.count() == 1
    assert NoteStore(path).notes[0].body == "Buy milk"
