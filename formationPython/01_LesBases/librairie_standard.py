# random - Génération d'aléatoire
import random
print(f"Un nombre aléatoire entre 0 et 15 exclu : {random.randrange(15)}")
print(f"Une dizaine aléatoire entre 0 et 100 : {random.randrange(0, 101, 10)}")
print(f"Un nombre aléatoire entre 10 et 15 : {random.randint(10,15)}")
print(f"Un nombre aléatoire entre 0 et 1 : {random.random()}")

# os - Pour modifier les fichiers et dossiers
import os
folder_path = os.path.join(os.path.curdir, "os-demo", "exportA")
print(f"Le chemin de mon dossier est : {folder_path}")
# os.makedirs(folder_path, exist_ok=True)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
if os.path.exists(folder_path):
    os.removedirs(folder_path)

# Pour obtenir de l'aide
print(dir(random))  # Pour obtenir la liste des fonctions contenues dans un module
#                       (les fonction avec underscore sont privées, attention)
help(random.randint)  # Pour lire la documentation de la fonction

# pprint - Pour clarifier la lecture des structures de données
from pprint import pprint
pprint(dir(random))

# Fonctions utiles
print(f"len('Python') => {len('Python')}")
print(f"round(2.6) => {round(2.6)}")
print(f"min([1, 2, 3]) => {min([1, 2, 3])}")
print(f"max([1, 2, 3]) => {max([1, 2, 3])}")
print(f"min('abc') => {min('abc')}")
print(f"max('abc') => {max('abc')}")
print(f"sum([1, 2, 3]) => {sum([1, 2, 3])}")
print(f"range(5) => {[x for x in range(5)]}")
