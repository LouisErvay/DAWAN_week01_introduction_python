import sqlite3

cnx = sqlite3.connect('database.db')

curseur = cnx.cursor()

req = "SELECT * FROM person"
curseur.execute(req)
personnes = curseur.fetchall()

for p in personnes:
    print(p)


curseur.close()
cnx.close()