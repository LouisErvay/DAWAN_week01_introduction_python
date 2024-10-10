# Pour manipuler un fichier à manipuler il y a 2 étapes:
# 1- Préparer le path dans une variable

import os
actual_folder = os.path.dirname(__file__)
file_path = os.path.join(actual_folder,"text.txt")

# 2- Ouvrir le fichier avec open()
# 'r' pour read, 'w' pour write, ou 'a' pour append
# Il faut penser à faire un file.close() à la fin

from mytools.filetool import lecture_fichier_texte,ecriture_fichier_texte

ecriture_fichier_texte(path=file_path, contenu="Bonjour")
print(lecture_fichier_texte(path=file_path))

print(os.getcwd())