"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.exceptions import InstantiateCSVError
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
    assert len(item_fixture.all) == 5


def test_instantiate_from_csv__FileNotFoundError(item_fixture):
    with pytest.raises(FileNotFoundError):
        item_fixture.instantiate_from_csv(csv_path='../src/it.csv')


def test_instantiate_from_csv__InstantiateCSVError(item_fixture):
    with pytest.raises(InstantiateCSVError):
        item_fixture.instantiate_from_csv(csv_path='../src/items_test.csv')


def test_string_to_number():
    assert Item.string_to_number('5.5') == 5


def test_name(item_fixture):
    item_fixture.name = 'Смартфон'
    assert item_fixture.name == 'Смартфон'


def test_name__exception(item_fixture):
    with pytest.raises(Exception):
        item_fixture.name = 'СуперСмартфон'


def test_repr(item_fixture):
    assert repr(item_fixture) == "Item('Булочка', 2.0, 8)"


def test_str(item_fixture):
    assert str(item_fixture) == 'Булочка'
