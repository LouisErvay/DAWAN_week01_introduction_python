# Un ensemble (set) est une collection non ordonnée sans doublons. De plus, le type set supporte les opérations sur les ensembles:
# telles l'union, l'intersection, la différence et la différence symétrique

# création d'ensemble :
e = set()

x = {"a","b","c","d","a","c"}
print(x)

a = set('abracadabra')
b= set("alacazam")

print(a)
print(b)

# Union -> Lettres dans A ou dans B ou dans les deux (toutes quoi)
print(a | b)
print(a.union(b))

# Intersection -> lettres dans A et dans B (lettres en commun)
print(a & b)
print(a.intersection(b))

# Différences -> Lettres dans A mais pas dans B
print(a - b)
print(a.difference(b))

# Différence symétrique -> Lettres dans A ou dans B mais pas dans les deux
print(a ^ b)
print(a.symmetric_difference(b))


ensemble = set("abracadabra")

# On veut un nouvel ensemble qui reprend celui de ensemble mais sans les lettres a, b et c:
resultat = {lettre for lettre in ensemble if lettre not in 'abc'}
