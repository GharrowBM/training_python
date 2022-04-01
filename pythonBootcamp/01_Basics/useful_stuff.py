# Usefull Functions
for _ in range(10):
    print("Hello")

for item in range(0,20,3):
    print(f"The number is {item}")

new_word = "abcdefghi"
for index, letter in enumerate(new_word):
    print(f"At Index {index}: {letter}")

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = ['a', 'b', 'c']
list_3 = list(zip(list_1, list_2))
for item in zip(list_1, list_2):
    print(item)

print(f"Is the letter 'a' in the list 'list_2' ? {'a' in list_2}")

from random import shuffle, randint # Import de fonctionnalités
list_to_shuffle = list(range(11))
print(f"Liste avant shuffle : {list_to_shuffle}")
shuffle(list_to_shuffle)
print(f"Liste après shuffle : {list_to_shuffle}")
print(f"Nombre aléatoire entre 0 et 11 : {randint(0,11)}")
input_number = int(input("Entrez un nombre : "))
print(f"Vous avez entré : {input_number}")

my_squared_number = []

for item in range(0,11):
    my_squared_number.append(item)
# Equals to
my_squared_numbers = [x**2 for x in range(0,11)]

print(f"my_squared_numbers = {my_squared_numbers}")
my_even_numbers = [x for x in range(21) if x % 2 == 0]
print(f"My_even_numbers = {my_even_numbers}")
celcius_values = [0, 10, 20, 34.5]
fahrenheit_values = [((9/5)*temp + 32) for temp in celcius_values]
for a,b in zip(celcius_values, fahrenheit_values):
    print(f"Celcius: {a}°C => Fahrenheit: {b}°F")

list_of_numbers = [x if x % 2 == 0 else 'ODD' for x in range(21)]
print(list_of_numbers)

my_multiplicated_numbers = []
for x in range(1,4):
    for y in range(10,31,10):
        my_multiplicated_numbers.append(x*y)
print(my_multiplicated_numbers)
# Equals to
my_list2 = [x*y for x in range(1,4) for y in range(10,31,10)]
print(my_list2)