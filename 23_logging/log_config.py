import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(filename)s - %(message)s",
    filename="app.log", # Si inexistant -> sera crée
    filemode='a',
    encoding='utf8',
    datefmt="%d-%m-%y - %h-%m" #Formatage de la date
)

try:
    10/0
except Exception as e:
    logging.error(e)