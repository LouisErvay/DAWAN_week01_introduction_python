# Bonne pratique :

# A chaque début de projet, on crée un environnement virtuel contenant les modules externes concernant le projet.
# Un environement virtuel est une copie de Python

# Pour créer un environnement virtuel, on utilise le module de base venv
# Note : Sous pycharm, à la création d'un nouveau projet un .venv est automatiquement crée par l'IDE

# 1-   Commande à exécuter dans le terminal:
# python -m venv "nom_de_environnement"

# 2-   Commande à exécuter dans le terminal:
# .\myenv\Script\activate

# A la fin du projet, on génère un fichier contenant la liste des modules externes utilisés dans le projet
# Commande à exécuter dans le terminal :
# pip freeze --local > requirements.txt
# Génère un fichier requirements.txt qui contient la liste de tous les modules du projet

# Commande à exécuter pour installer une liste d'un fichier txt:
# pip install -r requirements.txt