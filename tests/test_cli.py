import pytest
from smartcart.cli import run_console

def test_add_and_exit(monkeypatch, capsys):
    inputs = iter(["1", "banana", "0.99", "2", "7"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))


    run_console()

    output = capsys.readouterr().out
    assert "Item added." in output
    assert "Goodbye" in output

def test_update_item(monkeypatch, capsys):
    inputs = iter(["1", "apple", "1.00", "2", "3", "apple", "5", "7"])  # Add → Update → Exit
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    run_console()
    output = capsys.readouterr().out
    assert "Quantity updated." in output

def test_apply_valid_promo(monkeypatch, capsys):
    inputs = iter(["1", "apple", "10", "1", "5", "10OFF", "7"])  # Add → Apply promo → Exit
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    run_console()
    output = capsys.readouterr().out
    assert "Promo applied!" in output

def test_clear_cart(monkeypatch, capsys):
    inputs = iter(["1", "apple", "1.00", "1", "6", "4", "7"])  # Add → Clear → View → Exit
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    run_console()
    output = capsys.readouterr().out
    assert "Cart cleared." in output
    assert "Cart is empty." in output
