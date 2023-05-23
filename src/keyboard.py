from src.item import Item


class MixinLanguage:
    __language = 'EN'

    def __init__(self):
        self.__language = self.__language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new_language):
        if new_language not in ['EN', 'RU']:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")
        self.__language = new_language.upper()

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
            return self
        self.language = 'EN'
        return self


class KeyBoard(Item, MixinLanguage):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
