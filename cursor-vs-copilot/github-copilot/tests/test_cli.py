import pytest

from notes_manager_copilot_test.cli import main


@pytest.fixture
def db_path(tmp_path):
    return tmp_path / "notes.db"


def test_add_and_get(db_path, capsys):
    exit_code = main(
        ["--db", str(db_path), "add", "Title", "Body text", "--tags", "a", "b"]
    )
    assert exit_code == 0
    capsys.readouterr()

    exit_code = main(["--db", str(db_path), "get", "Title"])
    assert exit_code == 0
    output = capsys.readouterr().out
    assert "title: Title" in output
    assert "Body text" in output


def test_get_missing_returns_error(db_path, capsys):
    exit_code = main(["--db", str(db_path), "get", "Nope"])
    assert exit_code == 1


def test_search(db_path, capsys):
    main(
        ["--db", str(db_path), "add", "Shopping", "Buy milk", "--tags", "home"]
    )
    capsys.readouterr()

    exit_code = main(["--db", str(db_path), "search", "milk"])
    assert exit_code == 0
    output = capsys.readouterr().out
    assert "Shopping" in output


def test_list_tag(db_path, capsys):
    main(["--db", str(db_path), "add", "Note1", "Body1", "--tags", "work"])
    capsys.readouterr()

    exit_code = main(["--db", str(db_path), "list-tag", "work"])
    assert exit_code == 0
    output = capsys.readouterr().out
    assert "Note1" in output

    exit_code = main(["--db", str(db_path), "list-tag", "missing"])
    assert exit_code == 0
    output = capsys.readouterr().out
    assert "No notes found" in output
