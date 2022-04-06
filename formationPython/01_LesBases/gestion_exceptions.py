# La Gestion des Exceptions
a, b = 15, 0

try:
    print(f"{a} / {b} = {a / b}")
except ZeroDivisionError:
    print("Nous avons eu une erreur de division par zéro !")
except:
    print("Nous avons eu une erreur inconnue !")
else:
    print("Nous executons ce bloc s'il n'y a pas d'exceptions")
finally:
    print("Nous effectuons cette ligne peu importe s'il y a une exception ou non")
    