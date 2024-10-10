# 1) Définir une fonction qui renvoie la chaine inversée
# 2) Définir une fonction qui vérifie si une chaine est un palindrôme : sos, sms

def exo1(text):
    return text[::-1]

def exo2(text):
    text = text.lower()
    return text == exo1(text)


x = "abcdefg"
y = "radar"
print(exo1(x))
print(exo2(y))