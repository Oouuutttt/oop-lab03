class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.__stock = stock

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_stock(self):
        return self.__stock

    def set_stock(self, stock):
        self.__stock = stock