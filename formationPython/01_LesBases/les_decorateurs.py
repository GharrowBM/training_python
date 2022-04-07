# Stockage de fonction dans des variables
def say_hello():
    print("Hello")
    pass


g = say_hello  # On stocke une fonction dans une variable
del say_hello  # Malgré la suppression de la première fonction
g()  # On peut tout de même appeller g


# Fonction qui retourne une fonction en résultat
def hello(name: str='Arnold'):
    print("The hello() function has been executed!")

    def greet():
        return "\t This is the greet() function inside hello!"

    def welcome():
        return "\t This is the welcome() function inside hello!"

    print("I'm going to return a function!")

    if name == 'Arnold':
        return greet
    else:
        return welcome


result = hello(name='Marion')
print(result())


#  Un décorateur agit de sorte à augmenter les fonctionnalités
#  d'une fonction, par retour de la fonction avec ajout des fonctionnalités
def new_decorator(original_func):

    def wrap_func():
        print("Code before function")
        original_func()
        print("Code after function")
        pass

    return wrap_func


# En commentant simplement ce décorateur, on repasse à la fonction de base
@new_decorator
def func_needs_decorator():
    print("Not decorated function")
    pass


func_needs_decorator()
