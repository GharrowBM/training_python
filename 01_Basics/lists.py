# Les Listes
my_list = [1, "two", 3.0]
print(f"my_list = {my_list}")
my_list[1] = my_list[1].upper()
print(f"my_list = {my_list}")
my_list.append("Four".lower())
print(f"my_list = {my_list}")
popped_value = my_list.pop()
print(f"my_list = {my_list}")
print(f"popped value : {popped_value}")
my_list.pop(1)
print(f"my_list = {my_list}")
my_list.insert(1,"two")
print(f"my_list = {my_list}")
char_list = ['a', 'd', 'b', 'f', 'c', 'e']
num_list = [10,784,1,1278,1365]
print(f"Avant : {num_list}, Après : {num_list.sort()}")