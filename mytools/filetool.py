def lecture_fichier_texte(path:str) -> str:
    """Fonction de lecture du contenu d'un fichier texte

    Args:
        path: Chemin d'accès du fichier

    Returns:
        Str: Renvoie l'intégralité du fichier texte
    """
    try :
        with open(path, 'r', encoding="utf8") as file:
            return file.read()
    except Exception as e:
        print(f"Problème de lecture du fichier '{path}', erreur : {e}")

def ecriture_fichier_texte(path:str, contenu:str, overwrite:bool=True) -> None:
    """Fonction d'écriture à la fin d'un fichier texte

    Args:
        path: Chemin d'accès du fichier
        contenu: Texte à inssérer dans le fichier
        overwrite: True pour écraser le contenu du fichier avant l'écriture, False si non

    Returns:
    """
    try:
        with open(path, 'w' if overwrite else 'a', encoding="utf8") as file:
            file.write(contenu)
    except Exception as e:
        print(f"Problème d'écriture dans le fichier '{path}', erreur : {e}")