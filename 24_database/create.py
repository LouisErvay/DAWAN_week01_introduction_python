import sqlite3

cnx = sqlite3.connect('database.db')

curseur = cnx.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS person(
id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
nom varchar(30) NOT NULL,
prenom varchar(30) NOT NULL,
age int unsigned NOT NULL,
CONSTRAINT unique_names UNIQUE (nom,prenom)
)
""")

try:
    curseur.execute("INSERT INTO person(nom,prenom,age) VALUES ('DUPONT', 'Jean', 60)")

    # Dans la pratique il est recommander d'utiliser des commandes SQL paramétrées:
    # C'est une protection contre les injections SQL
    # Une commande SQL paramétrée est pré-complétée, chargée en mémoire en attente de params

    curseur.execute("INSERT INTO person values(NULL,?,?,?)",('CONNEY','Sean',75))

    cnx.commit()
except Exception as e:
    print(e)
    cnx.rollback() # -> le rollback annule toutes les commandes SQL

finally:
    curseur.close()
    cnx.close()