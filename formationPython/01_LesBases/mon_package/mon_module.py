
def mon_addition(a: int = 0, b: int = 0):
    # Docstring (documentation) au format Google
    """
    Fonction permettant l'addition de deux nombres entiers

    Args:
        a: Le premier nombre
        b: Le second nombre

    Returns:
        La somme des deux nombres
    """

    return a + b

if __name__ == "__main__":
    print(f"10 + 20 = {mon_addition(10, 20)}")
