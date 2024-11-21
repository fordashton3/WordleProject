import random
import csv
import os
import datetime
from colorama import  Fore, Style

def main():
    username = get_username()
    row = 0
    while is_playing(): # TODO main gameplay loop
        print_board(board)
        get_guess()
        for i in range(5):
            board[row][i] = guess[i]
        row += 1


def is_playing():
    if board[5][0] != "":
        return False
    elif answer == guess:
        return False
    else:
        return True

def is_valid_word(word):
    for i in range(len(possible_answers)):
        if word == possible_answers[i].upper():
            return True
    return False

def print_board(board):
    for word in board:
        print("----------------\n")
        for i in range(len(word)):
            print(f"| {format_letter(word, i)} ", end="")
        print("|")
    print("----------------")

def format_letter(word, letter_index): # Done, needs testing
    # Green if letter same position as answer
    if word[letter_index] == answer[letter_index]:
        return Fore.GREEN + word[letter_index] + Style.RESET_ALL

    # Yellow if letter is in answer
    for i in range(5):
        if word[letter_index] == answer[i]:
            return Fore.YELLOW + word[letter_index] + Style.RESET_ALL

    # Dim if letter not in answer
    return Style.DIM + word[letter_index] + Style.RESET_ALL

def get_word_array(input_file): # Done, needs testing
    with open(input_file, 'r') as infile:
        words = infile.read().strip().split(',')

        five_letter_words = [word.strip().upper() for word in words if len(word.strip()) == 5]
        return five_letter_words

def has_digit(string):
    for x in string:
        if not x.isalpha() and x != "." :
            return False
    return True

def get_username():
    username = input("Please enter your First name and Last initial (John D.): ")
    while has_digit(username):
        input(Fore.RED + "Error: Cannot have number in username." + Style.RESET_ALL)
        username = input("Please enter your First name and Last initial (John D.): ")
    return username

def add_score(username, score): # TODO - Write method for adding user score to leaderboard: Ben
    current_date = str(datetime.date.today())
    score_data = [current_date + " ", " Score: " + score] # TODO - add actual score variable
    file_name = username + ".csv"
    file_exists = os.path.exists(file_name)

    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter="|")
        if not file_exists:
            writer.writerow([username])
            writer.writerow([])

        writer.writerow(score_data)

def get_guess():
    guess=input("Enter a five letter word:").upper()
    while not is_valid_word(guess):
        guess=input("Enter another 5 letter word:").upper()





board = [["" for _ in range(5)] for _ in range(6)]
possible_answers = get_word_array("possibleAnswers.csv")
valid_words = get_word_array("validWords.csv")
answer = possible_answers[random.randint(0, len(possible_answers) - 1)]
guess = ""
main()
