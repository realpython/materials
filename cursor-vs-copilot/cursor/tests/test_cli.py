from notes_manager_cursor_test.cli import main


def run(tmp_path, *args):
    notes_dir = tmp_path / "notes"
    db_path = tmp_path / "notes.db"
    return main(["--notes-dir", str(notes_dir), "--db", str(db_path), *args])


def test_add_and_get(tmp_path, capsys):
    exit_code = run(
        tmp_path,
        "add",
        "My Note",
        "--tags",
        "foo,bar",
        "--body",
        "Hello world",
    )
    assert exit_code == 0

    exit_code = run(tmp_path, "get", "My Note")
    assert exit_code == 0
    out = capsys.readouterr().out
    assert "My Note" in out
    assert "foo, bar" in out
    assert "Hello world" in out


def test_get_missing_note_returns_error(tmp_path):
    assert run(tmp_path, "get", "Nope") == 1


def test_search(tmp_path, capsys):
    run(tmp_path, "add", "Trip Plan", "--body", "Visit the mountains")
    run(tmp_path, "add", "Unrelated", "--body", "Nothing relevant")
    capsys.readouterr()

    run(tmp_path, "search", "mountains")
    out = capsys.readouterr().out
    assert "Trip Plan" in out
    assert "Unrelated" not in out


def test_list_tag(tmp_path, capsys):
    run(tmp_path, "add", "Note A", "--tags", "red", "--body", "a")
    run(tmp_path, "add", "Note B", "--tags", "blue", "--body", "b")
    capsys.readouterr()

    run(tmp_path, "list-tag", "red")
    out = capsys.readouterr().out
    assert "Note A" in out
    assert "Note B" not in out


def test_list_all(tmp_path, capsys):
    run(tmp_path, "add", "Note A", "--body", "a")
    run(tmp_path, "add", "Note B", "--body", "b")
    capsys.readouterr()

    run(tmp_path, "list")
    out = capsys.readouterr().out
    assert "Note A" in out
    assert "Note B" in out
