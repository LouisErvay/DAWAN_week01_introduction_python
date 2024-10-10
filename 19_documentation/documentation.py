# Pour générer une doc en python, on utilise les 3 guillements : """ """
"""
Ceci est la doc de ce fichier
Patati patata..
"""
print(__doc__)

import math

print(math.__doc__)

#On peut aussi documenter les fonctions:
def addition(x:int,y:int) -> int:
    # La Syntaxe google - plus lisible et plus utilisé :
    """

    Args:
        x:
        y:

    Returns:

    """
    # Syntaxe de doc reST :
    """
    Fonction qui additionne
    :param x:
    :param y:
    :return:
    """
    # Il existe aussi la syntaxe EpyText:
    """
    Fonction qui additionne
    @param x: 
    @param y:
    @return: 
    """
    pass

print(addition.__doc__)

# Module de base de Python: pydoc
# -> python -m pydoc
