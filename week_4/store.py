class Item:
    def __init__(self, product_id, name, description, price, quantity):
        self.__product_id = product_id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__quantity = quantity

    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price >= 0:
            self.__price = price

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def increase_quantity(self, amount):
        self.__quantity += amount

    def decrease_quantity(self, amount):
        self.__quantity -= amount

    def __str__(self):
        return (
            f"Product: {self.__name}\n"
            f"Description: {self.__description}\n"
            f"Quantity: {self.__quantity}\n"
            f"Price: ${self.__price} each.\n"
            f"++++++++++++++++++++++++++++++++++++++++\n"
        )

class Store:
    def __init__(self, name, money):
        self.__store_name = name
        self.__money = money
        self.__products = []

    def get_store_name(self):
        return self.__store_name

    def set_store_name(self, store_name):
        self.__store_name = store_name

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def get_products(self):
        return self.__products

    def set_products(self, products):
        self.__products = products

    def add_products(self, products):
        self.__products.append(products)

    def __str__(self):
        string = ""
        for each in self.__products:
            string += (
                f"{self.__store_name}\n"
                f"Current Money We Have In Da Bank Boi: ${self.__money}\n"
                f"Current Stock We Have Boi: \n"
                f"++++++++++++++++++++++++++++++++++++++++\n"
                f"{each}"
            )
        return string


# Test the classes
car = Item(1, 'Car', "Ford", 10, 10)
flashlight = Item(2, "Flashlight", "It's a light", 69, 69)

newStore = Store("Shop", 100)
newStore.add_products(car)
newStore.add_products(flashlight)

print(newStore)
