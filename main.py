import products
import promotions
import store


def apply_choice(user_input, store_name):
    """apply choice by user.
    choice 1: list store products
    choice 2: prints total items in store
    choice 3: order option(ask for amount, and product order number)"""
    if user_input == "1":
        print(f"All store's products".upper())
        print("-----")
        for product_index, product in enumerate(store_name.products):
            print(f"{product_index + 1}. {product.show()}")
        print("-----")

    if user_input == "2":
        print(f"total items in store:".upper())
        print(store_name.get_total_quantity())

    if user_input == "3":
        print("When you want to finish order, enter empty text.")
        product_index = "1"
        while product_index != "".strip():
            try:
                product_index = input("Which product # do you want? :")
                if int(product_index) > len(store_name.get_all_products()):
                    print("There isn't a product responding to this choice")
                    continue
                try:
                    quantity = int(input("Enter amount: "))
                    if quantity < 0:
                        print("Amount must be positive number")
                        continue
                    order_price_amount = store_name.order([(store_name.products[int(product_index) - 1], quantity)])
                    print(f"Total purchase amount: {order_price_amount}")
                except products.QuantityException:
                    print("There are not enough products to buy!")
                except products.LimitedQuantityException:
                    print(f"Product is limited to {store_name.products[int(product_index) - 1].maximum}")
            except ValueError:
                print("Please enter an integer")


def start(store_name):
    """start program, print menu for the user"""
    user_input = ""
    while user_input != "4":
        print("\n"
              "1. List all products in store\n"
              "2. Show total amount in store\n"
              "3. Make an order\n"
              "4. Quit")
        user_input = input("Please choose a number: ")
        print("")
        apply_choice(user_input, store_name)
    print("Thank you for shopping at Best Buy:)")


def main():
    """purchasing program and manging stock"""
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
