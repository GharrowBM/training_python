# Une fonction en Python se déclare via l'utilisation du mot-clé DEF
from random import shuffle


def multiply_numbers(nbA: int = 1, nbB: int = 1):
    return nbA * nbB

print(f"5 * 2 = {multiply_numbers(5, 2)}")