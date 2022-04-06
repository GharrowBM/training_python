# Les fonctions se créent via l'utilisation de 'def'
def ma_fonction():
    print("j'exécute ma fonction")
    pass

def appeler_x(x:str):
    print(f"Coucou {x}")
    pass

def faire_somme(a:int, b:int):
    return a + b

ma_fonction()
appeler_x("Arnold")
print(f"5 + 2 = {faire_somme(5, 2)}")

# Le Scope
valeur_x = 50

def modifier_valeur(valeur_x:int):
    valeur_x *= 2
    print(f"Dans la fonction, la valeur vaut : {valeur_x}")
    pass

def modifier_valeur_globale():
    global valeur_x

    valeur_x *= 2
    print(f"Dans la fonction, la valeur vaut : {valeur_x}")
    pass

print("=== Valeur Locale ===")
print(f"Avant la fonction, la valeur vaut : {valeur_x}")
modifier_valeur(valeur_x)
print(f"Après la fonction, la valeur vaut : {valeur_x}")

print("=== Valeur Globale ===")
print(f"Avant la fonction, la valeur vaut : {valeur_x}")
modifier_valeur_globale()
print(f"Après la fonction, la valeur vaut : {valeur_x}")
