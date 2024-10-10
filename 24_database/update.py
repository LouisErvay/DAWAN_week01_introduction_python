import sqlite3

cnx = sqlite3.connect('database.db')

curseur = cnx.cursor()

# Les =: permettent d'avoir des paramètres nommés (toujours pour combattre les injections SQL)
req = "UPDATE person set nom=:last_name, prenom=:first_name, age=:age WHERE id=:id"

params = {
    'last_name': 'new_nom',
    'first_name': 'new_person',
    'age': 28,
    'id': 1
}

curseur.execute(req,params)
cnx.commit()


curseur.close()
cnx.close()