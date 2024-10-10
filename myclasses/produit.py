class Produit:

    def __init__(self, id, desc, price):
        self.id = id
        self.desc = desc
        self.price = price

    def __str__(self) -> str:
        return f"Identifiant : {self.id}, description : {self.desc}, prix : {self.price}"

    def __eq__(self, other: object) -> bool:
        return self.id == other.id