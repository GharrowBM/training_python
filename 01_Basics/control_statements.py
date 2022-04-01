# Booléens
print(6 > 3 == 3)

# IF / ELIF / ELSE
my_if_number = 5
if my_if_number > 10:
    print("The number is higher than 10")
elif my_if_number == 5:
    print("The number is equal to 5")
else:
    print(f"The number is {my_if_number}")

# FOR LOOPS
my_for_list = ["Bernie", 15, 3.5]
for item in my_for_list:
    print(f"The item is {item}")

my_for_dict = {'k1':"Bernie", 'k2':15, 'k3':3.5}
for a,b in my_for_dict.items():
    print(f"Key : {a}, VALUE : {b}")

# WHILE
x = 0
while x < 21:
    x+=1
    if x % 15 == 0:
        break # Stopper l'itération
    elif x % 3 == 0:
        continue # Passer à l'itération suivante
    elif x % 2 == 0:
        print(x)
    else:
        pass # Ne rien faire
else:
    print("We are out of the loop")