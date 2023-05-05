"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def item_fixture():
    return Item('Булочка', 2.0, 8)


def test_calculate_total_price(item_fixture):
    assert item_fixture.calculate_total_price() == 16.0


def test_apply_discount(item_fixture):
    item_fixture.apply_discount()
    assert 2.0 * Item.pay_rate == item_fixture.price
    assert item_fixture.price == 3.0


def test_instantiate_from_csv(item_fixture):
    item_fixture.instantiate_from_csv()
    assert len(item_fixture.all) == 8


def test_string_to_number():
    assert Item.string_to_number('5.5') == 5


def test_name(item_fixture):
    item_fixture.name = 'Смартфон'
    assert item_fixture.name == 'Смартфон'


def test_name__exception(item_fixture):
    with pytest.raises(Exception):
        item_fixture.name = 'СуперСмартфон'
