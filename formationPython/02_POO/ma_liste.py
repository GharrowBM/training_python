import json
import logging, os
from mes_constantes import DATA_DIR

LOGGER = logging.getLogger()

class Liste(list):  # Liste va hériter de 'list'
    def __init__(self, nom):
        self.nom = nom

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que des chaines de caractères !")

        if element in self:
            LOGGER.error(f"{element} fait déjà partie de la liste !")
            return False

        self.append(element)
        return True

    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False

    def afficher(self):
        print(f"Ma liste de {self.nom} :")
        for e in self:
            print(f" - {e}")

    def sauvegarder(self):
        path = os.path.join(DATA_DIR, f"{self.nom}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        with open(path, "w") as f:
            json.dump(self, f, indent=4)

        return True


if __name__ == '__main__':
    liste_courses = Liste('Courses')
    liste_courses.ajouter('Banane')
    liste_courses.ajouter('Banane')
    liste_courses.ajouter('Chocolat')
    liste_courses.ajouter('Vanille')
    liste_courses.ajouter('Fraise')
    liste_courses.ajouter('Chantilly')
    liste_courses.ajouter('Citron')
    print(liste_courses)
    liste_courses.enlever('Citron')
    print(liste_courses)
    liste_courses.sauvegarder()
