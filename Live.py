from Utils import ERROR_MESSAGE
from Utils import screen_cleaner
import time
import MemoryGame
import GuessGame
import Score


# This function gets user name as an input and returns a welcome message
def welcome():
    global name
    name = input("Please enter your name: ")
    print("Hello " + name + """ and welcome to the World of Games (WoG).
Here you can find many cool games to play.""")


# This function runs the corresponding game according to the user's input of game and difficulty
def load_game():
    global game, difficulty, points
    game = int(input("""Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
2. Guess Game - guess a number and see if you chose like the computer
1 or 2?: """))
    while game not in range(1, 3):
        valid_input()
        break
    else:
        difficulty = int(input("Please choose game difficulty from 1 to 5: "))
        if difficulty not in range(1, 6):
            valid_input()
    if game == 1:
        for i in range(1,6):
            if difficulty == i:
                MemoryGame.play_1(i)
                if MemoryGame.is_list_equal(MemoryGame.list_a, MemoryGame.list_b):
                    points = difficulty
                    Score.add_score(points)
                    Score.add_score_db(name, points)
                    play_again = input("Do you want to play again?, y/n: ")
                    if play_again == "y":
                        screen_cleaner()
                        load_game()
                else:
                    time.sleep(2)
                    screen_cleaner()
                    load_game()
    elif game == 2:
        for i in range(1,6):
            if difficulty == i:
                GuessGame.play_2(i)
                if GuessGame.compare_results(difficulty, GuessGame.secret_number):
                    points = difficulty
                    Score.add_score(points)
                    Score.add_score_db(name, points)
                    play_again = input("Do you want to play again?, y/n: ")
                    if play_again == "y":
                        screen_cleaner()
                        load_game()
                else:
                    time.sleep(2)
                    screen_cleaner()
                    load_game()


# This function is printing an error message
def valid_input():
    print(ERROR_MESSAGE)
