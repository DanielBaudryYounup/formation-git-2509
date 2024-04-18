from src.business import Client, Product


def test_buy_product_decrease_wallet_with_product_price():
    # given
    client = Client("Bob", 200)
    product = Product("Product 1", 50)

    # when
    client.buy_product(product)

    # then
    assert client.wallet == 150
