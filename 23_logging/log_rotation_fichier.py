import logging

from logging.handlers import RotatingFileHandler

# La class RotationFileHandler permet de créer un gestionnaire de journalisation qui lui donne la possibilité de faire tourner ses fichiers de logs en fonction de leurs taille.

logger = logging.getLogger("Rotation logger")
logger.setLevel(logging.INFO)

#maxBytes=0 -> taille illimitée (1 seul fichier de log) donc aucune rotation

file_handler = RotatingFileHandler(
    'rotation.log',
    mode='a',
    maxBytes=200,
    backupCount=5,
    encoding='utf8'
)

logger.addHandler(file_handler)

for i in range(10):
    logger.info(f"ouai ouai ouai {i}")