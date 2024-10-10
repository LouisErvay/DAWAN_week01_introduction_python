# Ecrire un script qui choisi un nombre aléatoire compris entre 1 et 100
# Demander à l'utilisateur de deviner le nombre aléatoire'
# 6 tentatives max
# on indique a chaque essai si c'est supp ou inf'

import random

def jeu_du_random(nombre_max):
    x = random.randint(1, nombre_max)
    y = 0
    for i in range(6):
        while True:
            try:
                y = int(input("essai de trouver le nombre ! "))
            except Exception as e:
                print(e)
            else:
                break
        if x == y:
            print("C'est le bon chiffre, que d'la chatte, mais GG")
            break
        else:
            print(f"Ton nombre est {"inférieur" if y < x else "supérieur"} au nombre d'origine")
    if x != y:
        print(f"Perdu, c'était: {x}, recommence !")

while True:
    demande = input("""Jouer au jeu de la devinette ?
    NON -> tapez "n"
    OUI -> tapez le nombre max à deviner
    """)
    if demande == "n":
        break
    else:
        try:
            demande = int(demande)
            jeu_du_random(demande)
        except Exception:
            print("input incorrect")