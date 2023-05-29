from abc import ABC, abstractmethod


class Promotion(ABC):
    name = "Promotion"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Applies the promotion to the given product and quantity.
        Returns the discounted price (float)."""
        pass


class SecondHalfPrice(Promotion):
    name = "Second Half Price!"

    def apply_promotion(self, product, quantity):
        """Applies the second half price promotion to the given product and quantity.
        Returns the discounted price (float)."""
        full_price_items = quantity // 2 + quantity % 2
        discounted_items = quantity // 2
        discounted_price = product.price * full_price_items + \
            discounted_items * product.price / 2
        return discounted_price


class ThirdOneFree(Promotion):
    name = "Third One Free!"

    def apply_promotion(self, product, quantity):
        """Applies the third one free promotion to the given product and quantity.
        Returns the discounted price (float)."""
        items_to_pay = (quantity // 3) * 2 + quantity % 3
        discounted_price = product.price * items_to_pay
        return discounted_price


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """Applies the percent discount promotion to the given product and quantity.
        Returns the discounted price (float)."""
        total_price = product.price * quantity
        return total_price * (1 - self.percent / 100)
