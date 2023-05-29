import pytest
import products
import promotions


def test_product_normal():
    blue_product = products.Product(name="Blue", price=10, quantity=200)
    assert blue_product.show() == f'{blue_product.name}, Price: {blue_product.price},' \
                                  f' Quantity: {blue_product.quantity}, Promotion: {blue_product.promotion}'


def test_invalid_empty_name():
    with pytest.raises(Exception):
        products.Product(name=" ", price=10, quantity=200)


def test_invalid_price():
    with pytest.raises(Exception):
        products.Product(name=" ", price=-10, quantity=200)


def test_invalid_quantity():
    with pytest.raises(Exception):
        products.Product(name=" ", price=10, quantity=-200)


def test_zero_quantity_makes_inactive():
    blue_product = products.Product(name="Blue", price=10, quantity=1)
    blue_product.buy(1)
    assert not blue_product.is_active()


def test_purchase_modify_quantity():
    blue_product = products.Product(name="Blue", price=10, quantity=2)
    blue_product.buy(1)
    assert blue_product.quantity == 1


def test_purchase_too_large():
    with pytest.raises(Exception):
        blue_product = products.Product(name="Blue", price=10, quantity=2)
        blue_product.buy(3)


def test_order_limited_product_normal():
    blue_product = products.LimitedProduct(name="Blue", price=10, quantity=250, maximum=1)
    blue_product.buy(1)


def test_order_limited_product_over_limit():
    with pytest.raises(Exception):
        blue_product = products.LimitedProduct(name="Blue", price=10, quantity=250, maximum=1)
        blue_product.buy(3)


def test_order_promotion_second_half():
    blue_product = products.Product(name="Blue", price=10, quantity=250)
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    blue_product.set_promotion(promotions.SecondHalfPrice(second_half_price))
    assert blue_product.promotion.apply_promotion(blue_product, 2) == 15.0


def test_order_promotion_percent_discount():
    blue_product = products.Product(name="Blue", price=10, quantity=250)
    discounted_ten_percent = promotions.PercentDiscount("Ten percent!", percent=10)
    blue_product.set_promotion(discounted_ten_percent)
    assert blue_product.promotion.apply_promotion(blue_product, 1) == 9.0


def test_order_promotion_third_free():
    blue_product = products.Product(name="Blue", price=10, quantity=250)
    third_free = promotions.ThirdOneFree("Third Free!")
    blue_product.set_promotion(promotions.ThirdOneFree(third_free))
    assert blue_product.promotion.apply_promotion(blue_product, 3) == 20.0


pytest.main()
