import random
import time
from Utils import screen_cleaner


global difficulty, winning, points


# This function generates several numbers between 1 to 101, the amount of the numbers is according to difficulty level
def generate_sequence(difficulty):
    global list_a
    list_a = []
    for i in range(difficulty):
        num = random.randint(1, 101)
        list_a.append(num)
    print(list_a)
    time.sleep(0.7)
    screen_cleaner()


# This function gets a guessed numbers from the user
def get_list_from_user(difficulty):
    global list_b
    list_b = []
    for i in range(difficulty):
        number = input("After seeing the numbers enter the numbers you saw, each one separated with 'ENTER': ")
        list_b.append(int(number))
    return list_b


# This function compares the generated numbers with the user guessed numbers and returns a boolean result
def is_list_equal(list_a, list_b):
    return list_a == list_b


# This function runs all functions together as a flowing game
def play_1(difficulty):
    generate_sequence(difficulty)
    get_list_from_user(difficulty)
    print(is_list_equal(list_a, list_b))
