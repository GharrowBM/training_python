class Dog:
    specie: str = "Dog"  # Attribut de classe
    dog_number: int = 0

    def __init__(self, name: str, breed: str, age: int):  # Constructeur de Dog
        self.name = name  # Création d'attribut d'instance et affectation
        self.breed = breed
        self.age = age
        Dog.dog_number += 1

    def __str__(self):  # Surcharge de la méthode __str__
        return f"Le chien {self.name}, de race {self.breed}, a {self.age} ans"


print(Dog.specie)
mon_chien = Dog('Ryu', 'Huskie', 4)
print(mon_chien)
print(mon_chien.age)
