"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item('Булочка', 2.0, 8)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 16.0


def test_apply_discount():
    item1.apply_discount()
    assert 2.0 * Item.pay_rate == item1.price
    assert item1.price == 3.0
