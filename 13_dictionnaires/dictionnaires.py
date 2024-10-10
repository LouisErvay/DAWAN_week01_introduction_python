# Un dictionnaire est une collection ordonnée qui fonctionne par association clé:valeur.
# Les clés sont uniques

# Initialiser un dict vide :
d = dict()
dict = {}

user = {
    'nom': 'DUPONT',
    'prenom': 'Jean',
    'age': 45
}
print(user['nom'])

# Dictionnaire Complexe:
utilisateur = {
    'nom': 'DUPONT',
    'prenom': 'Jean',
    'age': 45,
    'telephones': ['0606060606','0707070707'],
    'adresse': {
        'rue': 'rue de la fontaine',
        'numéro': 11,
        'code_postal': 31520
    }
}

for tel in utilisateur.get('telephones'):
    print(tel)

print(utilisateur.get('adresse').get('rue'))

# Créer une clé inexistante :
utilisateur['contrat'] = 'CDD'

# Modifier une info avec sa clé :
utilisateur['contrat'] = 'CDI'

# Les API Rest donnent leurs informations en JSON, qui correspond aux dict en python
#Les API REST ne sont pas limités au JSON, on peut avoir du text, du XML, img ect..

# Appel d'une API REST
# nécéssite le module requests

# import requests
#
# URI = "https://restcountries.com/v3.1/all"
#
# data = requests.get(URI).json()
# for pays in data:
#     print(f"Nom: {pays.get('name').get('common')} - Capitale: {pays.get('capital')[0]}")

d = {
    'a':1,
    'b':2
}

#Inverser clé / valeurs:
result = {v:k for k,v in d.items()}

