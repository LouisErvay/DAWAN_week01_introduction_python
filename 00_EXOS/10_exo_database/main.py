import logging
import log_manager
import db_produit

db_produit.init()

while True:
    choix = input("""Choisir une option parmis:
1- Voir tous les produits
2- Voir un produit particulier
3- Ajouter un produit
4- Modifier un produit
5- Supprimer un produit
6- Quitter
""")
    if choix == '6':
        break

    match choix:
        case '1':
            data = db_produit.get_all()
            for prod in data:
                print(f"Produit numéro {prod[0]}, {prod[1]}, au prix de {prod[2]}€.")
        case '2':
            data = db_produit.get_produit_by_id(id=int(input("Quel ID de produit voulez-vous voir ?")))
            print(f"Produit numéro {data[0]}, {data[1]}, au prix de {data[2]}€.")
        case '3':
            nom = input("Le nom du produit ?")
            prix = int(input("Le prix du produit ?"))
            db_produit.insert(nom=nom, prix=prix)
        case '4':
            id = int(input("Quel ID de produit modifier ?"))
            nom = input("Le nouveau nom du produit ?")
            prix = int(input("Le nouveau prix du produit ?"))
            db_produit.update(id=id, nom=nom, prix=prix)
        case '5':
            id = int(input("Quel ID de produit supprimer ?"))
            db_produit.delete(id)
