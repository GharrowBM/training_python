def player_guess():
    guess = -1
    while guess not in list(range(5)):
        guess = int(input("Pick a number from 0 to 4: "))
    return guess

def shuffle_list(list: list[str]):
    new_list = list
    shuffle(new_list)
    return new_list

def check_guess(list: list[str], guess: int):
    guess_result = False
    if list[guess] == 'x':
        print("You've won ! Congratulations !")
        guess_result = True
    else:
        print("Wrong guess, try again !")
    return guess_result

guess = -1
cups = ['x', '', '', '', '']

while True:
    cups = shuffle_list(cups)
    guess = player_guess()
    if check_guess(cups, guess): break