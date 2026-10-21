import pytest

from weatherly.cli import main


def test_main_prints_forecast(capsys):
    main(["lisbon", "--days", "1"])
    assert "Forecast for Lisbon:" in capsys.readouterr().out


def test_main_exits_on_invalid_days():
    with pytest.raises(SystemExit) as error:
        main(["lisbon", "--days", "0"])
    assert error.value.code == 1
