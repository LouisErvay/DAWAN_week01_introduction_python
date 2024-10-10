# 1) Afficher tous les nombres de 1 à 10 (inclus)
# 2) Afficher tous les nombres pairs de 1 à 10 (inclus)
#
# 3) Afficher le menu :
# choix = input("""
# Menu:
# Votre choix:
# 1) Convertir minutes en heures
# 2) Quitter
# """)
# Si 1 -> demander la saisie d'un nombre de min à convertir et afficher le résultat
# tant que y'a pas eu 2 continuer
#
# 4) Afficher le menu
# operation = input("""
# Choisir une opération:
# - Addition : tapez a
# - Soustraction: tapez s
# - Multiplication: tapez m
# - Division: tapez d
# - Quitter: tapez q
# """)
# Tant que le choix saisi n'est pas valide, repeat
# Tant que c'est pas q continuer
# Si non saisie de 2 nombres et afficher résultat, et repeat


i=1
while i <= 10:
    print(i)
    i += 1

i=1
while i <= 10:
    if i%2 == 0:
        print(i)
    i += 1

while True:
    choix = input("""Menu:
    Votre choix:
    1) Convertir minutes en heures
    2) Quitter
    """)
    if choix == "1":
        minutes = int(input("Combien de min voulez-vous convertir en heures ? "))
        heure = int(minutes / 60)
        restant = minutes % 60
        print(f"{minutes} minutes font {heure} heure{'s' if heure > 1 else ''} et {restant} minutes")
    elif choix == "2":
        break


while True:
    operation = input("""Choisir une opération:
    - Addition : tapez a
    - Soustraction: tapez s
    - Multiplication: tapez m
    - Division: tapez d
    - Quitter: tapez q
    """)
    match operation:
        case "a":
            print(f"Le résultat de l'addition est: {int(input("Le premier nombre à additioner ?")) + int(input("Le second nombre à additioner ?"))}")
        case "s":
            print(f"Le résultat de la soustraction est: {int(input("Le nombre de base ?")) - int(input("Le nombre à soustraire à celui de base ?"))}")
        case "m":
            print(f"Le résultat de la multiplication est: {int(input("Le premier nombre à multiplier ?")) * int(input("Le second nombre à multiplier ?"))}")
        case "d":
            print(f"Le résultat de la division est: {int(input("Le premier dividende ?")) / int(input("Le second nombre diviseur ?"))}")
        case "q":
            break