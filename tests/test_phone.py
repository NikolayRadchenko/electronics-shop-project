from src.phone import Phone
from src.item import Item
import pytest


@pytest.fixture
def phone_fixture():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def item_fixture():
    return Item("Смартфон", 10000, 20)


def test_src(phone_fixture):
    assert str(phone_fixture) == 'iPhone 14'


def test_repr(phone_fixture):
    assert repr(phone_fixture) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(phone_fixture):
    assert phone_fixture.number_of_sim == 2


def test_number_of_sim__value_error(phone_fixture):
    with pytest.raises(ValueError):
        phone_fixture.number_of_sim = 0


def test_add(phone_fixture, item_fixture):
    assert item_fixture + phone_fixture == 25
    assert phone_fixture + phone_fixture == 10
