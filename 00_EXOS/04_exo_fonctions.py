# 1) Définir une fonction qui renvoie la somme d'une liste d'entiers
# 2) Définir une fonction qui renvoie la moyenne d'une liste d'entiers
# 3) Définir une fonction qui renvoie l'élément le plus petit d'une liste d'entiers

# 4) Definir une fonction qui affiche une table de multiplication avec en params le premier et dernier multiple
# 5) Afficher menu avec choix de 2 fonction:
#     convertir heures en minutes
#     convertir minutes en heures
#     quitter

import random

def somme(list):
    x = 0
    for number in list:
        x += number
    return x

def moyenne(list):
    return somme(list) / len(list)

def smallest(list):
    x = list[0]
    for number in list:
        x = number if x > number else x
    return x

def hours_to_minutes(hours,minutes):
    print(f"{hours * 60 + minutes} minutes")

def minutes_to_hours(minutes):
    print(f"{int(minutes/60)} heures et {minutes%60} minutes")

def multiply_table(base, start=1, end=10):
    for i in range(end-start+1):
        print(f"{base} * {start+i} = {base*(start+i)}")

list = []
for i in range(10):
    list.append(random.randint(1,100))

print(list)
print(somme(list))
print(moyenne(list))
print(smallest(list))

while True:
    demande = input(""" Choisisez entre les 3 options :
    1) Convertir les heures en minutes
    2) Convertir les minutes en heures
    3) Voir une table de multiplication
    4) Quitter    """)
    if demande not in ["1","2","3","4"]:
        print("seulement 1, 2, 3 ou 4")
        continue

    match demande:
        case "1":
            hours_to_minutes(int(input("combien d'heures à convertir ?")), int(input("des minutes en plus ?")))

        case "2":
            minutes_to_hours(int(input("Combiens de minutes à convertir en heures ?")))

        case "3":
            multiply_table(base=int(input("Quelle table ?")), start=int(input("de ?")), end=int(input("à ?")))

        case "4":
            break