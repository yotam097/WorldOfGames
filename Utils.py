import os


SCORES_FILE_NAME = "Scores.txt"
file_write = open(SCORES_FILE_NAME, "a")
file_read = open(SCORES_FILE_NAME, "r")


ERROR_MESSAGE = "Something went wrong.."


# This function is cleaning the screen
def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

