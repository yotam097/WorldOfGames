import random

global winning, points


# This function generates a number between 1 to difficulty
def generate_number(difficulty):
    global secret_number
    secret_number = random.randint(1, difficulty)
    return secret_number


# This function gets a guessed number from the user
def get_guess_from_user(difficulty):
    global guess
    guess = input("Please guess a number from 1 to " + str(difficulty) + ": ")
    return guess


# This function compares the generated number with the user guessed number and returning a boolean result
def compare_results(difficulty, secret_number):
    return int(secret_number) == int(guess)


# This function runs all functions together as a flowing game
def play_2(difficulty):
    generate_number(difficulty)
    get_guess_from_user(difficulty)
    print(compare_results(difficulty, secret_number), "; The number is: ", secret_number)

