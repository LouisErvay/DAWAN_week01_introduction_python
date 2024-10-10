age = 25
prenom = 'louis'

# Concaténation fstring (c'est la meilleure utilise que celle la)
print(f"Prénom : {prenom}; Age : {age}")

# Chaines multi-lignes :
print("""Ligne 1
Ligne 2
Ligne 3""")

# Caractères d'échappement :
# \n -> retour à la ligne
# \t -> tabulation
# \s -> space
# \b -> back space
# \\ -> ignorer le \

x = "des \"guillemets\" ici"
print(x)