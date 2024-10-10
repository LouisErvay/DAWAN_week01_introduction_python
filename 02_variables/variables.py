# Une variable c'est quoi :
#Ca stock des données dans la RAM du pc

# Déclaration de variables :
# Typage dynamique : Pas besoin de spécifier le type de la variable
# Exemple : (Python -> x = 10) (JAVA -> int x = 10)

#Type numériques : int, float, complex
#Type textuels : str (string)
#Type boolean : True or False
#Type listes : range, tuple, list
#Type ensemble : set
#Type mapping : dict (dictionnaire)

entier = 10
nombre_a_virgule = 10.63
complexe = 4 + 2j # Avec J le nombre imaginaire
text = "chaine"
je_vais_bien = True

# Conventions de nommage pour les variables
# Le nom doit commencer par une lettre
# Pas de majuscules
# PascalCase -> MaVariable
# camelCase  -> maVariable
# snake_case -> ma_variable -> Utilisé par python
# Python est case sensitive -> age et Age sont deux variables différentes

# Constante : En principe, est une variable dont le contenu ne peut pas etre modifié
# En python, elle peut être modifiée, une constante revient donc plus à être une convention de nommage
VITESSE_LUMIERE_MS = 299_800_000

# Variable nulles :
vide = None

# Vérifier le type des variables :
print(f"Type de la variable float : {type(float)}")
print(f"Type de la variable text : {type(text)}")

# Emplacement mémoire identiques pour 2 variables stockant la même valeur
x = 10
y = 10
print(f"x = {id(x)} et y = {id(y)}")

# L'écriture des nombres float est libre : .99 = 0.99 = 00.99

# Pour la lisibilité des grands nombres, on peut ajouter des "_" au millieu d'un nombre :
v = 969_785_456

# Convertion de type :
entier = 15
x = float(entier)
print(x)

float = 10.55
print(int(float))

# RANDOM
import random

x = random.randint(5,15) # rend un nombre aléatoire entre 5 et 15
print(x)