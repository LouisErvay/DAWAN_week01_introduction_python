import logging

# On peut logger plusieurs types d'informations :
# - Informations de débug : C'est pour la partie dev
# - Informations générales (updates d'un produit, login de quelqu'un ect..)
# - Informations pour indiquer une erreur:
#   * Warning : erreur mineure
#   * Error : pour indiquer un problème (Exception)
#   * Critical : Pour indiquer une erreur critique (arrêt de l'app)

# 5 niveaux de message: debug -> info -> warning -> error -> critical

# Par défaut, ce module utilise le niveau warning pour les messages
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")