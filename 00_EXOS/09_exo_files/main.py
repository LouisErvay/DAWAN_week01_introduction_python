#Parcourrir le dossier en cour, lire tous les fichiers .txt et sauvegarder le contenu dans un nouveau fichier new.txt

import os
from mytools.filetool import lecture_fichier_texte,ecriture_fichier_texte

actual_folder = os.getcwd()
new = ""
for e in os.listdir(actual_folder):
    y = os.path.splitext(e)
    if y[1] == ".txt":
        x = lecture_fichier_texte(os.path.join(actual_folder,e))
        new += f"""Dans le fichier '{y[0]}' il y a:
{x}

"""

ecriture_fichier_texte(os.path.join(actual_folder,"new.txt"), contenu=new)