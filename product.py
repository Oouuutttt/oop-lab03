class Product:
    def __init__(self, name, price, stock, discount):
        self.name = name
        self.__price = price
        self.__stock = stock
        self.discount = discount

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Цена должна быть больше 0")

    def get_stock(self):
        return self.__stock

    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            print("Количество товара не может быть меньше 0")

    def calculate_price_with_vat(self):
        price_with_vat = self.__price * 1.20
        return price_with_vat

    def calculate_final_price(self):
        price_with_vat = self.calculate_price_with_vat()
        final_price = price_with_vat - price_with_vat * self.discount / 100
        return final_price