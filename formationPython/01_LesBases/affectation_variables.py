def get_int_from_user(prompt:str):
    '''
    Fonction pour récupérer une valeur numérique saisie par l'utilisateur
    :param prompt: le message à afficher à l'utilisateur
    :return: la valeur numérique entrée par l'utilisateur
    '''
    while True:
        try:
            result = int(input(prompt))
        except ValueError:
            print("Valeur incorrecte, veuilliez recommencer !")
        else:
            return result


# Affectation simple
a = 5
b = 7

# Affectation parallèle (souvent pour inverser les deux variables)
a, b = b, a

# Affectation multiple
c = d = e = 9

# Pour récupérer des valeurs utilisateur
user_input = input("Donnez une valeur SVP : ")
print(f"Vous avez donné comme valeur : {user_input}, qui est de type : {type(user_input)}")
int_input = int(input("Donnez un INT SVP : "))
print(f"Vous avez donné comme valeur {int_input}, qui est de type : {type(int_input)}")
int_secured = get_int_from_user("Veuilliez entrer un nombre SVP : ")
print(f"Vous avez donné comme valeur {int_secured}")
