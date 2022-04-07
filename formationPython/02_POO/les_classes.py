class Mammal:
    specie: str = "Mammal"  # Attribut de classe
    mammal_number: int = 0

    def __init__(self, name: str, age: int):  # Constructeur de Mammal
        self.name = name  # Création d'attribut d'instance et affectation
        self.age = age
        Mammal.mammal_number += 1

    def __str__(self):
        return f"Le mammifère {self.name} a {self.age} ans"

class Dog(Mammal):  # Héritage de Mammal pour Dog
    specie: str = "Dog"
    dog_number: int = 0

    def __init__(self, name: str, breed: str, age: int):
        super().__init__(name, age)  # Appel au constructeur de la classe parent
        self.breed = breed
        Dog.dog_number += 1

    def __str__(self):  # Surcharge de la méthode __str__
        return f"Le chien {self.name}, de race {self.breed}, a {self.age} ans"

    # Pour créer plus facilement certains types d'instances,
    # on utilise les méthodes de classe, comme ici pour créer un husky
    @classmethod
    def huskie(cls):
        return cls("Rex", "Husky", 1)

    # Pour utiliser les variables de classe (statiques),
    # il faut utiliser le décorateur @staticmethod
    @staticmethod
    def afficher_nombre_chiens():
        print(f"Vous avez {Dog.dog_number} chiens dans votre chenil.")


print(Dog.specie)
mon_chien = Dog.huskie()
print(mon_chien)
print(mon_chien.age)
mon_chien.afficher_nombre_chiens()
