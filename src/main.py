from business import Client, Product
from src.business import NotEnoughMoney


def main():
    product1 = Product("Produit 1", 60)
    product2 = Product("Produit 2", 100)
    available_products = [product1, product2]

    firstname = input("Quel est votre prénom ?")
    client = Client(firstname, 300)
    print(f"Bonjour {firstname}, votre solde est de : {client.wallet}\n")

    client_is_online = True

    while client_is_online:
        print("Que voulez-vous acheter ?\n")
        for product in available_products:
            print(f"1) {product.name} - {product.product_type} ({product.price}€)\n")
        print("0) Quitter\n")
        choice = input("Votre choix ?\n")

        if choice == "0":
            client_is_online = False
        elif choice == "1":
            try:
                client.buy_product(product1)
            except NotEnoughMoney:
                print("Pas assez d'argent")
        elif choice == "2":
            try:
                client.buy_product(product2)
            except NotEnoughMoney:
                print("Pas assez d'argent")

    print("A bientôt !")


if __name__ == '__main__':
    main()
