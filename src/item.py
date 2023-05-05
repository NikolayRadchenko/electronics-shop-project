import csv


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

    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Item(row['name'], float(row['price']), int(row['quantity']))

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
