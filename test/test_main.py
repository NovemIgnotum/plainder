import pytest
import builtins
import datetime
from main import to_galactic, get_greeting
from main import main

def test_to_galactic_basic():
    assert to_galactic("abc") == "ᔑʖᓵ"
    assert to_galactic("Hello!") == "⍑ᒷꖎꖎ𝙹¡"
    assert to_galactic("123") == "123"
    assert to_galactic("Bonjour") == "ʖ𝙹リ⋮𝙹⚍∷"

def test_to_galactic_unknown_char():
    assert to_galactic("abc$") == "ᔑʖᓵ$"

def test_get_greeting_morning(monkeypatch):
    class MockDate(datetime.datetime):
        @classmethod
        def now(cls):
            return cls(2024, 1, 1, 10, 0, 0)
    monkeypatch.setattr(datetime, "datetime", MockDate)
    assert get_greeting() == to_galactic("Bonjour")

def test_get_greeting_evening(monkeypatch):
    class MockDate(datetime.datetime):
        @classmethod
        def now(cls):
            return cls(2024, 1, 1, 20, 0, 0)
    monkeypatch.setattr(datetime, "datetime", MockDate)
    assert get_greeting() == to_galactic("Bonsoir")

def test_main_palindrome(monkeypatch, capsys):
    inputs = iter(["kayak"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    monkeypatch.setattr("main.get_greeting", lambda: "SALUT")
    main()
    out = capsys.readouterr().out
    assert "kayak" in out or "ᓭᔑꖎ⚍ℸ" in out  # Output should contain the palindrome

def test_main_non_palindrome(monkeypatch, capsys):
    inputs = iter(["hello"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    monkeypatch.setattr("main.get_greeting", lambda: "SALUT")
    main()
    out = capsys.readouterr().out
    assert "hello" in out or "⍑ᒷꖎꖎ𝙹" in out  # Output should contain the input