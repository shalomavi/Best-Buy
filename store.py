from typing import List

import products


class Store:
    def __init__(self, list_of_products):
        self.products = list_of_products

    def add_product(self, product):
        """Adds product to store"""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        total_products = 0
        if len(self.products) == 0:
            return total_products

        for product in self.products:
            total_products += product.get_quantity()

        return total_products

    def get_all_products(self) -> List[products.Product]:
        """Returns a list of all products in the store that are active."""
        list_of_active_products = []
        for product in self.products:
            if product.is_active():
                list_of_active_products.append(product)

        return list_of_active_products

    def order(self, shopping_list: List) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class), and quantity (int).
        Buys the products and returns the total price of the order."""
        total_order_price = 0.0
        for product_index, (product_class, product_quantity) in enumerate(shopping_list):
            product_price = product_class.buy(product_quantity)
            total_order_price += product_price
        return total_order_price
