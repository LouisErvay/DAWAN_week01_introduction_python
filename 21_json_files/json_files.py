import os
import json

json_file_path = os.path.join(os.path.dirname(__file__), 'users.json')

# Lecture du fichier json
with open(json_file_path, 'r', encoding='utf8') as flux:
    for user in json.load(flux):
        print(f"name: {user.get('name')}, lat: {user.get('address').get('geo').get('lat')}")

# Ecriture du fichier json
new_json_file_path = os.path.join(os.path.dirname(__file__), 'new.json')
with open(new_json_file_path, 'w', encoding='utf8') as flux:
    data = {
        "python": "Language de programmation",
        "version": 3.12
    }

    json.dump(data, flux, indent=4, ensure_ascii=False) # Si ensure_ascii = True -> tous les non ascii seront ignorés

# Exo : A partir de user.json, construire un nouveau resultat.json contenant seulement le username et le mail
data = []
with open(json_file_path, 'r', encoding='utf8') as flux:
    for user in json.load(flux):
        data.append({
            "username": user['username'],
            "email": user['email']
        })

exo_json_file_path = os.path.join(os.path.dirname(__file__), 'resultat.json')
with open(exo_json_file_path, 'w', encoding='utf8') as flux:
    json.dump(data, flux, indent=2, ensure_ascii=False)