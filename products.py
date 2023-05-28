class QuantityException(Exception):
    if __name__ == "__main__":
        print("Quantity Error")


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """Initiator (constructor) method.
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity),
        raises an exception."""
        if name.strip() == "":
            raise Exception("Empty name value Error, Please enter a name")
        if price < 0:
            raise Exception("Negative price Error, please set price again")
        if quantity < 0:
            raise Exception("Negative quantity Error, please set quantity again")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """Getter function for quantity.
        Returns the quantity (float)"""
        return float(self.quantity)

    def set_quantity(self, quantity: int):
        """Setter function for quantity.
         If quantity reaches 0, deactivates the product."""
        if type(quantity) is not int or quantity < 0:
            raise QuantityException("Invalid input Error, insert quantity again")
        self.quantity = quantity
        if self.quantity <= 0:
            self.active = False

    def is_active(self) -> bool:
        """Getter function for active.
        Returns True if the product is active,
        otherwise False."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """Returns a string that represents the product"""
        return f'{self.name}, Price: {self.price}, Quantity: {self.quantity}'

    def buy(self, quantity: int) -> float:
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase."""
        if quantity == "" or not type(quantity) is int or quantity < 0:
            raise QuantityException("Invalid input Error, insert quantity again")
        if self.quantity - quantity < 0:
            raise QuantityException("Quantity Error, there are not enough products to buy")
        self.set_quantity(self.quantity - quantity)
        if self.quantity == 0:
            self.deactivate()
        return float(self.price * quantity)


class NonStockedProduct(Product):
    def __init__(self, name, price, quantity=0):
        super().__init__(name, price, quantity)

    def show(self) -> str:
        """Returns a string that represents the product"""
        return f'{self.name}, Price: {self.price}, Quantity: Unlimited'

    def buy(self, quantity: int) -> float:
        """Buys a given quantity of the product, quantity is unlimited.
                Returns the total price (float) of the purchase."""
        if quantity == "" or not type(quantity) is int or quantity < 0:
            raise QuantityException("Invalid input Error, insert quantity again")
        self.set_quantity(0)
        return float(self.price * quantity)


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self) -> str:
        """Returns a string that represents the product"""
        return f'{self.name}, Price: {self.price}, Limited to {self.maximum} per order!'

    def buy(self, quantity: int) -> float:
        """Buys a given quantity of the product.
                Returns the total price (float) of the purchase."""
        if quantity == "" or not type(quantity) is int or quantity < 0:
            raise QuantityException("Invalid input Error, insert quantity again")
        if self.quantity - quantity < 0:
            raise QuantityException("Quantity Error, there are not enough products to buy")
        if quantity > self.maximum:
            raise QuantityException(f"Quantity Error, product limited to {self.maximum} per order!")
        if self.quantity == 0:
            self.deactivate()
        return float(self.price * quantity)
