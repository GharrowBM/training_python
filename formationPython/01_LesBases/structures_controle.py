# Les structures conditionnelles
age = int(input("Veuilliez donner un âge :"))
if 21 <= age <= 100:  # Equivaut à age >= 21 and age <= 100
    print("La personne est majeure aux USA")
elif age >= 10:
    print("La personne est majeure en France")
else:
    print("La personne est mineure")

# Les structures de répétition
list = [1, 2, 3, 4, 5]
print("Contenu du list : ")
for item in list:
    print(item)

print("Contenu indéxé de list :")
for item, index in enumerate(list):
    print(f"{index} : {item}")

print("Dire 5 fois bonjour : ")
for _ in range(5):
    print("Hello")

while True:
    result = input("Veuilliez écrire STOP pour quitter : ")
    if result == 'STOP':
        break
    elif result.upper() == 'STOP':
        print("Attention à la casse !")
        continue
    else:
        pass

while result != 'STOP':
    print("result est différent de STOP")
    result = 'STOP'
else:
    print("Nous sommes en dehors de la boucle !")
    