# Les collections python sont des itérables
# Il y a 2 types d'itérables :
#   Ordonnées (listes, tuples, string)
#   Non ordonnées (set, dictionnaire)

# Fonction enumerate -> permet de parcourir une collection

chaine = "test"

for i in enumerate(chaine):
    print(i) # i est un tuple (element, index)

for index, element in enumerate(chaine):
    print(f"element {element}, index {index}")


# Valeurs des variables True ou False

# Valeurs True :
# Un nombre n'importe lequel; une chaine non vide ("..."); Une collection non vide
# En bref toutes variables qui porte quelque chose dedans

# Valeurs False:
# le nombre 0; un chaine vide (""); Une collection vide []

x = [1,0,1,0]
y = [1,1,1,1]

# Fonction all() -> qui vérifie si toutes les valeurs sont True dans une collection
# Si une seule valeur est False -> return False
print(all(x)) # --> False
print(all(y)) # --> True

# Fonction any() -> Vérifie si au moins une valeur est True dans une collection
# Si une seule valeur est True -> return True
print(any(x)) # --> True
print(any(y)) # --> True