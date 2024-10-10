# Un module doit etre importé avant son utilisation
# Différents types d'imports :

# import random
# import random as rd
# from random import randint
# from random import randint as random_int
# from random import *

# Un module est un fichier python .py
# Un package est un répertoire contenant des modules

# /!\ Le nom d'un package doit etre en minuscule sans espaces ni _ : ceciestmonpackage

# Pour convertir un dossier en package -> il faut ajouter un fichier "__init__.py" dedans

from packageexample.module import my_function
my_function()

print(__name__)
# __name__ contient __main__ si c'est le fichier à l'origine de l'exécution, si non le nom du module

# Dans un module, on va utiliser le if __name__ == "__main__":... pour tester les fonctions définies dans le module.
# Ce if n'est pas amené à etre utilisé par la suite.