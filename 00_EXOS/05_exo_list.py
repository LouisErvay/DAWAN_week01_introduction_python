# 1) prendre une liste range(-10,10) et n'en retirer qu'une liste de nombre positif
# 2) prendre une liste range(10) et faire devenir tous els nombres impairs négatifs

# 3) list = [1,5,3,7,9]
# Afficher le nombre d'éléments suppérieux à 3

# 4)
# list_a = [1,2,3,4]
# list_b = [1,2]
# Afficher la différence entre ces deux listes
#
# 5) Définir une fonction qui prend en paramètres une liste d'entiers et qui renvoie la somme des entiers pairs distincts

list = range(-10,10)
list_1 = [e for e in list if e > 0]
print(f"liste seulement positive : {list_1}")

list = range(10)
list_2 = [e if e % 2 == 0 else -e for e in list]
print(f"pair positif / impairs négatif : {list_2}")

list = [1,5,3,7,9]
list_supp_a_trois = [e for e in list if e > 3]
print(f"Il y a {len(list_supp_a_trois)} d'éléments suppérieurs à 3, les voici : {list_supp_a_trois}")

list_a = [1,2,3,4]
list_b = [1,2]
difference = [e for e in list_a if e not in list_b]
print(difference)

def somme_entiers_pair_distincts(list:[]) -> int:
    return sum(set([e for e in list if e % 2 == 0]))

list = [1,2,2,3,5,6,6,7,8,9,4,4,4,4]
print(somme_entiers_pair_distincts(list))