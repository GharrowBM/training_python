# Les list comprehensions
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"INIT => ma_liste = {ma_liste}")
ma_liste = [x for x in range(0, 21)]
print(f"[x for x in range(0, 21)] => ma_liste = {ma_liste}")
ma_liste = [x**2 for x in range(0, 11)]
print(f"[x**2 for x in range(0, 11)] => ma_liste = {ma_liste}")
ma_liste = [x for x in range(0, 21) if x % 2 == 0]
print(f"[x for x in range(0, 21) if x % 2 == 0] => ma_liste = {ma_liste}")
ma_liste = ['E' if x % 2 == 0 else 'O' for x in range(0, 11)]
print(f"['E' if x % 2 == 0 else 'O' for x in range(0, 11)] => ma_liste = {ma_liste}")
