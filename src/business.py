class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Client:
    def __init__(self, name: str, wallet: int):
        self.name = name
        self.wallet = wallet

    def buy_product(self, product: Product):
        if self.wallet >= product.price:
            print("Produit acheté !")
            self.wallet = self.wallet - product.price
