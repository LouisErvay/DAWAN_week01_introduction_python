# En développement, il y a 2 type de scripts / languages :
# Procéduraux -> Repose sur l'utilisation des paramètres et de fonctions
# Objets -> Repose sur l'utilisation de classes et d'objets

# C'est une approche de résolution de problèmes algorithmique permettant de produire des programmes modulaires.

# Objectifs :
# - Développer l'application sans qu'il soit nécéssaire de connaitre les détails internes des autres parties
# - Réutiliser des fragements de codes dans un cadre différent
# - Apporter des modifications à un module sans que cela n'affècte le reste du programme

# Objet: est une élément identifiable du monde réel: abstrait ou concrèt.
# - possède une identité
# - un état: les propriété de l'objet
# - un comportement: les fonctions de l'objet

# Classe : est un type de donnée, dont la tâche principale est de décrire la structure d'un objet. Elle définie
# le template à partir duquel on crée nos objets

# Elle contient généralement 3 éléments :
# - attributs (propriétés)
# - fonctions
# - fonctions spéciale qui porte le nom de la classe appelée constructeur (initialisateur -> __init__)
# Permet d'instancier la classe en question

class User:

    profile = "Stagiaire"

    def __init__(self, first_name='', last_name='', age=18):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def comment_je_mappelle(self):
        return f"Je m'appelle {self.first_name} {self.last_name} !"

    @classmethod
    def modifier_profile(cls,profile):
        cls.profile = profile

u = User("Jean", "Gertrude")
print(u.comment_je_mappelle())

print(u.profile)
User.modifier_profile("RH")
print(u.profile)


class CompteBancaire:

    banque = 'BNP'

    def __init__(self, numero, solde) -> None:
        self.numero = numero
        self.solde = solde

    def depot(self, amount):
        self.solde += amount

    def retrait(self, amount):
        self.solde -= amount

    @classmethod
    def changer_banque(cls, nom_banque):
        cls.banque = nom_banque


def virement(compte_emeteur:CompteBancaire, compte_receveur:CompteBancaire, amount):
    compte_emeteur.retrait(amount)
    compte_receveur.depot(amount)

compte1 = CompteBancaire(numero=1, solde=1000)
compte2 = CompteBancaire(numero=2, solde=1000)

virement(compte1, compte2, 500)

print(compte1.solde)
print(compte2.solde)

#Convertir un objet en format dictionnaire :
print(compte2.__dict__)