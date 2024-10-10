import sqlite3

cnx = sqlite3.connect('database.db')

curseur = cnx.cursor()

req = 'INSERT INTO person VALUES (NULL,:nom,:prenom,:age)'
params = {
    'nom': 'bonsoir',
    'prenom': 'commenva',
    'age': 25
}

try:

    curseur.execute(req, params)
    cnx.commit()
except Exception as e:
    print(e)

curseur.close()
cnx.close()