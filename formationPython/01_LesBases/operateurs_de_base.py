# Les opérateurs mathématiques de base
nbA, nbB = 15, 4
print(f"L'addition de {nbA} et {nbB} donne : {nbA + nbB}")
print(f"La soustraction de {nbA} et {nbB} donne : {nbA - nbB}")
print(f"La multiplication de {nbA} et {nbB} donne : {nbA * nbB}")
print(f"La division de {nbA} et {nbB} donne : {nbA / nbB}")
print(f"La division entière de {nbA} et {nbB} donne : {nbA // nbB}")
print(f"Le modulo de {nbA} et {nbB} donne : {nbA % nbB}")
print(f"Le nombre {nbA} à la puissance {nbB} donne : {nbA ** nbB}")

# L'incrémentation en Python
i = 0
i += 1  # Equivaut à i = i + 1

# Les opérateurs de comparaison
print(f"{nbA} plus grand que {nbB} ? {nbA > nbB}")
print(f"{nbA} plus petit que {nbB} ? {nbA < nbB}")
print(f"{nbA} plus grand ou égal à {nbB} ? {nbA >= nbB}")
print(f"{nbA} plus petit ou égal à {nbB} ? {nbA <= nbB}")
print(f"{nbA} égal à {nbB} ? {nbA == nbB}")
print(f"{nbA} différent de {nbB} ? {nbA != nbB}")

# Différence entre == et 'is'
list_a = [1, 2, 3]
nombre_a, nombre_b = 10, 10
list_b = [1, 2, 3]
print(f"La liste 'list_a' a comme adresse mémoire {id(list_a)} et contient {list_a}")
print(f"La liste 'list_b' a comme adresse mémoire {id(list_b)} et contient {list_b}")
print(f"list_a == list_b ? {list_a == list_b}")  # Contient les même valeurs ?
print(f"list_a is list_b ? {list_a is list_b}")  # A la même adresse mémoire ?
print(f"nombre_a is nombre_b ? {nombre_a is nombre_b}")  # Les nombres entre -5 et 256 ont déjà des adresses mémoires
