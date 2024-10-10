import sqlite3
import logging

DATABASE_PATH = 'database.db'
def init():
    cnx = sqlite3.connect(DATABASE_PATH)
    curseur = cnx.cursor()

    curseur.execute("""
        CREATE TABLE IF NOT EXISTS produit(
        id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        nom varchar(30) NOT NULL,
        prix real NOT NULL
        )
        """)

    produits = [
        {'nom':'Souri', 'prix':45},
        {'nom': 'Clavier', 'prix': 40},
        {'nom': 'Ecran', 'prix': 90},
        {'nom': 'PC Gamer', 'prix': 1400}
    ]
    try:

        req = "INSERT INTO produit VALUES (NULL, :nom, :prix)"

        for p in produits:
            curseur.execute(req,p)
            logging.info(f"Un produit à été ajouté en base de donnée: {p['nom']}")

        cnx.commit()

    except Exception as e:
        logging.error(f"Erreur lors de l'ajout des produits dans l'init : {e}")
    finally:
        curseur.close()
        cnx.close()

def get_all():
    cnx = sqlite3.connect(DATABASE_PATH)
    curseur = cnx.cursor()

    data = []
    try:
        req = "SELECT * FROM produit"

        curseur.execute(req)

        data = curseur.fetchall()

    except Exception as e:
        logging.error(f"Erreur lors de la récupération de tous les produits : {e}")

    finally:
        curseur.close()
        cnx.close()

    return data


def get_produit_by_id(id):
    cnx = sqlite3.connect(DATABASE_PATH)
    curseur = cnx.cursor()

    data = {}
    try:
        req = f"SELECT * FROM produit WHERE id={id}"

        curseur.execute(req)

        data = curseur.fetchone()

    except Exception as e:
        logging.error(f"Erreur lors de la récupération du produit id {id}, erreur: {e}")

    finally:
        curseur.close()
        cnx.close()

    return data

def insert(nom:str, prix:int):
    cnx = sqlite3.connect(DATABASE_PATH)
    curseur = cnx.cursor()

    try:
        req = "INSERT INTO produit VALUES (NULL, :nom, :prix)"
        p = {
            'nom': nom,
            'prix': prix
        }
        curseur.execute(req, p)
        logging.info(f"Un produit à été ajouté en base de donnée: {p['nom']}")

        cnx.commit()

    except Exception as e:
        logging.error(f"Erreur lors de l'ajout des produits dans l'init : {e}")
    finally:
        curseur.close()
        cnx.close()

def update(id:int,nom:str,prix:int):
    cnx = sqlite3.connect(DATABASE_PATH)
    curseur = cnx.cursor()

    try:
        req = "UPDATE produit SET nom=:nom, prix=:prix WHERE id=:id"
        p = {
            'nom': nom,
            'prix': prix,
            'id': id
        }
        curseur.execute(req, p)
        logging.info(f"Le produit id {id} a été modifié en DB")

        cnx.commit()

    except Exception as e:
        logging.error(f"Erreur lors de la modification du produit ID {id}, erreur: {e}")
    finally:
        curseur.close()
        cnx.close()

def delete(id):
    cnx = sqlite3.connect(DATABASE_PATH)
    curseur = cnx.cursor()

    try:
        req = "DELETE FROM produit WHERE id=?"
        p = (id,)
        curseur.execute(req, p)
        logging.info(f"Le produit id {id} a été supprimé de la DB")

        cnx.commit()

    except Exception as e:
        logging.error(f"Erreur lors de la suppression du produit ID {id}, erreur: {e}")
    finally:
        curseur.close()
        cnx.close()
