from classes import Vendeur, Technicien, Representant
from fonctions import insert, afficher_salaire_all, afficher_tous_les_employes, afficher_salaire_moyen

while True:

    choix = input("""Choisir une opération:
    1- Afficher la liste des employés
    2- Insérer un employé
    3- Afficher le salaire de chacun des employé
    4- Afficher le salaire moyen
    5- Quitter
""")

    if choix == '5':
        break

    match choix:
        case '1':
            afficher_tous_les_employes()

        case '2':
            while True:
                type_employe = input("""Choisir quel type d'employé vous voulez rentrer dans la base de donnée :
    1- Vendeur
    2- Représentant
    3- Technicien
    4- Annuler
""")

                if type_employe == '4':
                    break
                elif type_employe in ['1','2','3']:
                    e = object
                    nom = input("Quel est son nom ?")
                    prenom = input("Quel est son prénom ?")
                    age = int(input("Quel est son age ?"))
                    match type_employe:
                        case '1' | '2':
                            ca = int(input("Quel est son CA ?"))
                            if type_employe == '1':
                                e = Vendeur(nom=nom, prenom=prenom, age=age, ca=ca)
                            else:
                                e = Representant(nom=nom, prenom=prenom, age=age, ca=ca)

                        case '3':
                            heures = int(input("Quel est son taux horraire mensuel ?"))
                            e = Technicien(nom=nom, prenom=prenom, age=age, heures=heures)
                    insert(e)
                    break
                else:
                    print("Choisir parmis les 4 options")

        case '3':
            afficher_salaire_all()

        case '4':
            afficher_salaire_moyen()