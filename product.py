class Product:
    _discount = 0

    def __init__(self, name, price):
        self.name = name
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price

    @classmethod
    def get_discount(cls):
        return cls._discount

    @classmethod
    def set_discount(cls, discount):
        if discount > 0:
            cls._discount = discount

    @property
    def current_price(self):
        return self._price * (1 - self._discount / 100)

    @staticmethod
    def create_fix_price(name):
        return Product(name, 99)

    def __str__(self):
        return f"{self.name} - {self.get_price()} рублей"