# Des fonctions quoi..
def fonction1():
    print("la 1")

fonction1()

print(fonction1) # print l'ID de la fonction en mémoire

f = fonction1
f()

# le typage des paramètres et du return
def somme (x:int, y:int) -> int:
    return x+y

# (ca marche aussi avec les variables)
g:int = 10

list = [10,20,30]

sum(list) # Somme des éléments de la liste
min(list) # Le plus petit élément
max(list) # Le plus grand élément
len(list) # Nombre d'éléments
