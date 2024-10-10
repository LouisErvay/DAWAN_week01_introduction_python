# Liste est une collection ordonnée avec doublons autorisés

#Liste vide:
list = []

from random import randint, choice, choices, sample, shuffle

for i in range(10):
    list.append(randint(1, 100))
print(list)

# Slicing (coupure de listes)
list1 = list[0:3]   # donne un liste de l'index de 0 à 2
list2 = list[:6]    # donne un liste du début jusquà index 5
list3 = list[:]     # du début jusqu'à la fin (copie)
list4 = list[0:4:2] # de l'index 0 à 3 par saut de 2
list5 = list[::2]   # du début jusqu'à la fin par saut de 2

list_double = [e * 2 for e in list]
print(list_double)

list_impairs = [e for e in list if e%2 != 0]
print(list_impairs)

# Choisi un élément aléatoire de a liste
print(choice(list))

# Choisi plusieurs éléments aléatoire de al liste selon k
print(choices(list, k=5))
print(sample(list, k=5)) # j'ai pas compris la différence avec choices mdr

# Mélange une liste dans un ordre désordonné
shuffle(list)
print(list)