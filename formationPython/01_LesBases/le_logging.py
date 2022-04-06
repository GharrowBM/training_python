# Pour afficher des informations en fonction du niveau de dangerosité
import logging, os

logs_folder_path = os.path.join(os.path.curdir, "logs")

if not os.path.exists(logs_folder_path):
    os.makedirs(logs_folder_path)

logging.basicConfig(level=logging.ERROR,  # On choisi le niveau minimal de logging
                    filename="./logs/first.log",  # On choisi où seront stockés les logs
                    filemode='a',  # On choisi le mode d"ouverture du fichier de logs
                    encoding='utf-8',  # On choisi l'encodage du fichier
                    format='%(asctime)s - %(levelname)s - %(message)s')  # On formate le texte des logs

# Les niveaux en ordre croissant
logging.debug("La fonction a bien été executée")
logging.info("Message d'info")
logging.warning("Attention !")
logging.error("Une erreur a été rencontrée")
logging.critical("Problème grave !!!")