import sqlite3

cnx = sqlite3.connect('database.db')

curseur = cnx.cursor()

req = "DELETE FROM person WHERE id=?"
param = (2,)

curseur.execute(req,param)
cnx.commit()

curseur.close()
cnx.close()