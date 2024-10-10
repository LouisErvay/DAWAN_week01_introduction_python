class Adresse:

    def __init__(self, number, street):
        self.number = number
        self.street = street

class Client:

    def __init__(self, name:str, adresse:Adresse):
        self.name = name
        self.adresse = adresse

c = Client('Henry', Adresse(15,'rue randomiter'))