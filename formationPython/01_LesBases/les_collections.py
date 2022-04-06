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
