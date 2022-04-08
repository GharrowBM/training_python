# Les Listes
nouvelle_liste = []
print(f"INIT => nouvelle_liste : {nouvelle_liste}")
nouvelle_liste2 = [1, 2, 'a', 'b', 3.5, 9.89]
nouvelle_liste.extend(nouvelle_liste2)  # Ajouter liste à une liste
print(f"EXTEND(list) => nouvelle_liste : {nouvelle_liste}")
nouvelle_liste.append("Nouvelle valeur")  # Ajouter un élément à une liste
print(f"APPEND(item) => nouvelle_liste : {nouvelle_liste}")
result = nouvelle_liste.pop()  # Retirer dernier élément de la liste
print(f"POP(-1) => nouvelle_liste : {nouvelle_liste}")
result = nouvelle_liste.pop(2)  # Retirer élément X dans la liste
print(f"POP(2) => nouvelle_liste : {nouvelle_liste}")
nouvelle_liste.remove(2)
print(f"REMOVE(2) => nouvelle_liste : {nouvelle_liste}")
nouvelle_liste.clear()
print(f"CLEAR() => nouvelle_liste : {nouvelle_liste}")


# Le tranchage [debut:fin:pas]
nouvelle_liste = [4, 1, 5, 1, 2, 2, 7, 2, 3, 10, 3, 3, 3]
print(f"nouvelle_liste[0] : {nouvelle_liste[0]}")
print(f"nouvelle_liste[-1] : {nouvelle_liste[-1]}")
print(f"nouvelle_liste[:2] : {nouvelle_liste[:2]}")
print(f"nouvelle_liste[1:3] : {nouvelle_liste[1:3]}")
print(f"nouvelle_liste[::-1] : {nouvelle_liste[::-1]}")

# Autres méthodes de listes
print(f"nouvelle_liste : {nouvelle_liste}")
print(f"INDEX(2) => nouvelle_liste : {nouvelle_liste.index(2)}")
print(f"COUNT(3) => nouvelle_liste : {nouvelle_liste.count(3)}")
print(f"SORTED() => nouvelle_liste : {sorted(nouvelle_liste)}")
print(f"nouvelle_liste : {nouvelle_liste}")
nouvelle_liste.sort()
print(f"SORT() => nouvelle_liste : {nouvelle_liste}")
nouvelle_liste.reverse()
print(f"REVERSE() => nouvelle_liste : {nouvelle_liste}")

# Joindre / Couper une liste
joined_list = " - ".join(["Hello", "I'm", "a", "sentence"])
print(f"' - '.JOIN => nouvelle_liste : {joined_list}")
splitted_list = joined_list.split(" - ")
print(f"SPLIT(' - ') => nouvelle_liste : {splitted_list}")

# Vérifier la présence dans une liste
ma_liste = ["Chien", "Chat", "Canard"]
mon_mot = "Javascript"
print(f"Est-ce que {ma_liste} possède 'Chat' : {'Chat' in ma_liste}")
print(f"Est-ce que {mon_mot} possède 'Java' : {'Java' in mon_mot}")

# Listes imbriquées
liste_imbrik = [1, 2, 3, 4, [1, 2, 3, 4, 5], [6]]
print(f"INIT => liste_imbrik : {liste_imbrik}")
print(f"liste_imbrik[4] : {liste_imbrik[4]}")
print(f"liste_imbrik[4][1:3] : {liste_imbrik[4][1:3]}")

# Les Dictionnaires
mon_dict = {0: {"prenom": "Paul",
                "profession": "Ingénieur civil",
                "ville": "Paris"},
            1: {"prenom": "Marie",
                "profession": "Pêcheuse",
                "ville": "Marseille"},
            2: {"prenom": "Sandra",
                "profession": "Architecte décoratrice",
                "ville": "Toulouse"}}
print(f"mon_dict : {mon_dict}")
print(f"mon_dict[1]['ville'] : {mon_dict[1]['ville']}")
print(f"mon_dict.get('ville', 'Pas de valeur') : {mon_dict[1].get('ville', 'Pas de valeur')}")
print(f"mon_dict[0] : {mon_dict[0]}")
mon_dict[0]['ville'] = "Poitiers"
print(f"mon_dict[0] : {mon_dict[0]}")
mon_dict[0]['age'] = 43
print(f"mon_dict[0] : {mon_dict[0]}")
if 'age' in mon_dict[0]:
    del mon_dict[0]['age']
print(f"mon_dict[0] : {mon_dict[0]}")

# Boucler sur un dictionnaire
for x in mon_dict.keys():
    print(x)
for x in mon_dict.values():
    print(x)
for x in mon_dict.items():
    print(x)
for k, v in mon_dict.items():
    print(f"KEY : {k}, VALUE : {v}")


# Les Sets (Permettant de retirer les doublons par exemple)
my_set = set()
my_set.add("Bernie")
my_set.add(3.5)
my_set.add(666)
print(f"my_set : {my_set}")
strange_list = [1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]
strange_set = set(strange_list)
print(f"strange_set : {strange_set}")


# Les Tuples (Immutables contrairement aux listes)
my_tuple = (1, "Bernie", 3.5)
print(f"my_tuple : {my_tuple}")
print(f"my_tuple[1] : {my_tuple[1]}")
print(f"my_tuple.count('a') : {my_tuple.count('a')}")
print(f"my_tuple.index('Bernie') : {my_tuple.index('Bernie')}")

#  L'unpacking des Tuples
chiffre, nom, chiffre_virgule = my_tuple
print(chiffre)
print(nom)
print(chiffre_virgule)


#  Les retours multiples via utilisation de Tuples
def ma_fonction(a: int, b: int):
    somme = a + b
    produit = a * b

    return a, b


somme, produit = ma_fonction(5, 10)
print(f"La somme de 5 + 10 vaut {somme} et le produit de 5 * 10 vaut {produit}")
