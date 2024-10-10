from classes import Employe,Vendeur,Representant,Technicien

employes:[Employe] = []

employes.append(Vendeur("LeBoucher","Didier",42,27800))
employes.append(Representant("TendRien","Jean",28,16340))
employes.append(Technicien("Erable","Miss",26,140))
employes.append(Technicien("DesLivres","Julie",62,228))

def insert(e: Employe):
    employes.append(e)

def afficher_salaire_all():
    for e in employes:
        print(f"Pour {e.prenom}, {e.calculer_salaire()} !")

def afficher_tous_les_employes():
    if employes:
        print("Aucun enployés enregistrés !")
    else:
        for e in employes:
            print(e.get_nom())

def afficher_salaire_moyen() -> float:
    x = 0
    for e in employes:
        x += e.calculer_salaire()
    print(x/len(employes))