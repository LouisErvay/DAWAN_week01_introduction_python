# Bon boucles for et while quoi..

# Mot clé break -> casse la boucle
i = 1
while i < 10 :
    print(i)
    if i == 5:
        break
    i += 1

# Mot clé continue -> Passe à l'itération suivante
i = 0
while i < 10 :
    i += 1
    if i == 5:
        continue
    print(i)