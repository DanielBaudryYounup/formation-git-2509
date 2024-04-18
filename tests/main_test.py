import pytest

from src.business import Client, Product, NotEnoughMoney


def test_buy_product_decrease_wallet_with_product_price():
    # given
    client = Client("Bob", 200)
    product = Product("Product 1", 50)

    # when
    client.buy_product(product)

    # then
    assert client.wallet == 150


def test_buy_product_decrease_wallet_until_empty():
    # given
    client = Client("Bob", 100)
    product = Product("Product 1", 100)

    # when
    client.buy_product(product)

    # then
    assert client.wallet == 0


def test_buy_product_should_raise_exception_when_not_enough_money():
    # given
    client = Client("Bob", 100)
    product = Product("Product 1", 200)

    # when
    with pytest.raises(NotEnoughMoney):
        client.buy_product(product)

    # then
    assert client.wallet == 100

