import csv
from src.exceptions import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.5
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.price = price
        self.__name = name
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None

    @classmethod
    def instantiate_from_csv(cls, csv_path='../src/items.csv'):
        cls.all = []
        try:
            with open(csv_path) as file_items:
                items = csv.DictReader(file_items, delimiter=',')
                for row in items:
                    if row['name'] and row['price'] and row['quantity']:
                        cls(row['name'], row['price'], row['quantity'])
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл item.csv")
            raise
        except InstantiateCSVError:
            print(f"InstantiateCSVError: Файл {csv_path} поврежден")
            raise

    @staticmethod
    def string_to_number(string):
        return int(float(string))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception("Длина наименования товара превышает 10 символов.")
        self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
