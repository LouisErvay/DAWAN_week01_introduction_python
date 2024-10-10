# 1) Demander la saisie d'un mot. Afficher un dictionnaire dont les clés sont les lettres du mot et les valeurs sont le nombre de chaque lettres dans le mot
# ex: "test" -> {'t':2, 'e':1, 's':1}

# 2) Définir une fonction qui prend en paramètres une liste d'entiers et qui rend un dict dont les clés sont les éléments
#  de la liste et les valeurs sont pair ou impair selon la parité de l'élément en question


def dict_compteur(text):
    x = {}
    for lettre in text:
        x[lettre] = text.count(lettre)
    return x

def dict_parite(list):
    y = {}
    for i in list:
        y[i] = "Pair" if i%2 == 0 else "impair"
    return y

text = "test ahah"
print(dict_compteur(text))

list = range(10)
print(dict_parite(list))