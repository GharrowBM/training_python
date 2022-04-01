def is_there_even_number(list:list[int]):
    result = False
    even_numbers = []
    for item in list:
        if(item % 2 == 0):
            result = True
            even_numbers.append(item)
    return result, even_numbers

my_list = []
input_nbr = 0
while input_nbr != -1:
    input_nbr = int(input("Give a number (-1 to cancel) : "))
    if (input_nbr != -1):
        my_list.append(input_nbr)

if (len(my_list) > 0):
    print(f"Are there any even numbers in the list ? {my_list}")
    test, numbers = is_there_even_number(my_list)
    if test:
        print(f"Yes, here are all the even numbers : {numbers}")
    else:
        print("No")