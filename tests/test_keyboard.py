from src.keyboard import KeyBoard
import pytest


@pytest.fixture
def keyboard_fixture():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_str(keyboard_fixture):
    assert str(keyboard_fixture) == "Dark Project KD87A"


def test_language(keyboard_fixture):
    assert str(keyboard_fixture.language) == "EN"


def test_change_lange(keyboard_fixture):
    keyboard_fixture.change_lang()
    assert str(keyboard_fixture.language) == "RU"


def test_mixin(keyboard_fixture):
    keyboard_fixture.change_lang().change_lang()
    assert str(keyboard_fixture.language) == "EN"


def test_change_lange__attribute_error(keyboard_fixture):
    with pytest.raises(AttributeError):
        keyboard_fixture.language = 'CH'
        