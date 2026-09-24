print("Hello! Welcome to the number guessing game.\nTry to guess the hidden number!\n ")
from random import randint

num = randint(1, 100)


def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100


def num_input():
    while True:
        n = input("Enter a number from 1 to 100. ")
        if is_valid(n):
            return int(n)
        print("Let's better enter a number from 1 to 100. ")


counter = 0

while True:
    user_num = num_input()
    counter += 1
    if num == user_num:
        print()
        print("You guessed it! Well done!")
        break
    elif num < user_num:
        print("You didn't guess right, the number is smaller. Try again.\n")
    else:
        print("You didn't guess right, the number is higher. Try again.\n")

print(f"You guessed correctly on the {counter} try. The number was {num}.\nThanks for the game! :)")
