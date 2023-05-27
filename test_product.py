import pytest
import products


def test_product_normal():
    blue_product = products.Product(name="Blue", price=10, quantity=200)
    assert blue_product.show() == f'{blue_product.name}, Price: {blue_product.price}, Quantity: {blue_product.quantity}'


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


pytest.main()
