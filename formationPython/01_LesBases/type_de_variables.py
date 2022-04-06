# Les Chaines de caractères
my_string = "Hello world"
print(f"my_string : {my_string}")

first_name = "Mark"
my_formatted_string = "Hello {}".format(first_name)
my_formatted_string2 = "Hello {0}".format(first_name)
my_f_string = f"Hello {first_name}"
print(f"my_formatted_string : {my_formatted_string}")
print(f"my_formatted_string2 : {my_formatted_string2}")
print(f"my_f_string : {my_f_string}")

# Les Integers (Nombres entiers)
my_integer = 25
my_hex_number = hex(25)
my_hex_number2 = 0xff
my_bin_number = bin(25)
my_bin_number2 = 0b10111
print(f"my_integer : my_integer")
print(f"my_hex_number : {my_hex_number}")
print(f"my_hex_number2 : {my_hex_number2}")
print(f"my_bin_number : {my_bin_number}")
print(f"my_bin_number2 : {my_bin_number2}")

# Les floats (Nombres décimaux)
my_float = 3.14
print(f"my_float : {my_float}")
print(f"my_float : {my_float:8.4f}")

# Les Booléens
my_bool = True
print(f"my_bool : {my_bool}")