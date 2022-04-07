# Les générateurs servent à renvoyer plusieurs valeurs
# que l'on peut parcourir sans les stocker en RAM
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result


#  Ici, on ne se sert pas d'un générateur
result_a = create_cubes(10)
print(f"result_a : {result_a}")
for x in result_a:
    print(x)


# Ici, on créé un générateur, qui est plus efficiant pour la RAM
# lorsque l'on souhaite juste parcourir des valeurs retournées à la suite
def create_square_generator(n):
    for x in range(n):
        yield x**3


result_b = create_square_generator(10)
print(f"result_b : {result_b}")
for x in result_b:
    print(x)


# Les générateurs se servent en réalité d'une fonction next()
# pour passer à la variable suivante, et du temps
# que l'on n'atteind pas le StopIteration, cela peut continuer
result_c = create_square_generator(3)
print(next(result_c))
print(next(result_c))
print(next(result_c))
# print(next(result_c))


#  Pour rentre un objet en iterateur, on peut utiliser iter(),
#  comme ici pour une string
s_iter = iter("Blabla")
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))