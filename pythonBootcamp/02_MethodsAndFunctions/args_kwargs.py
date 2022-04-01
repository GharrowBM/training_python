def sum_of_numbers(*args:int):
    return sum(args)
def fav_fruit(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")
    else:
        print("I didn't find any fruit in here")

def other_func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"I would like {args[0]} {kwargs['food']}")

print(sum_of_numbers(1,3,6))
fav_fruit(fruit="apple", veggie="bean")
other_func(10, 20, 30, food='steak', animal='cat')