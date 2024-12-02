import random
import csv
import os
import datetime
from colorama import  Fore, Style
from termcolor import colored

def main():
    username = get_username()
    row = 0
    print(answer) #for testing purposes - remove later
    print_board(board)
    guess = get_guess()
    for i in range(5):
        board[row][i] = guess[i]
    row += 1
    while is_playing(guess): # TODO main gameplay loop
        print_board(board)
        guess = get_guess()
        for i in range(5):
            board[row][i] = guess[i]
        row += 1

    score = ""
    if (guess == answer.upper()):
        score = str(row)
        print("\nCongratulations, You Won!")
    else:
        score = "Failed!"
        print("\nSorry, You Lost.")

    add_score(username, score)
    update_leaderboard(username, score)
    print("Game over. Score: " + score)
    print("Correct answer: " + answer + "\n")
    print_leaderboard()


def is_playing(guess):
    if board[5][0] != " ":
        print_board(board)
        return False
    elif guess == answer.upper():
        print_board(board)
        return False
    else:
        return True

def is_valid_word(word):
    for i in range(len(possible_answers)):
        if word == possible_answers[i].upper():
            return True
    return False

def print_board(board):
    print("\nWORDLE GAME")
    for word in board:
        print("---------------------")
        for i in range(len(word)):
            print(f"| {format_letter(word, i)} ", end="")
        print("|")
    print("---------------------")

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
    folder_path = "score-tracking-files"
    current_date = str(datetime.date.today())
    score_data = [current_date + " ", " Score: " + score] # TODO - add actual score variable
    file_name = username + ".csv"
    full_path = os.path.join(folder_path, file_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_exists = os.path.exists(full_path)
    with open(full_path, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter="|")
        if not file_exists:
            writer.writerow([username])
            writer.writerow([])

        writer.writerow(score_data)

def update_leaderboard(username, score):
    if score == "Failed!":
        return
    
    leaderboard_file = "leaderboard.csv"
    leaderboard = []
    with open(leaderboard_file, mode="r", newline="") as file:
        reader = csv.reader(file)
        leaderboard = list(reader)
    
    header = leaderboard[0]
    data = leaderboard[1:]
    user_found = False
    for row in data:
        if row[0] == username:
            user_found = True
            if int(score) < int(row[1]):
                row[1] = str(score)
            break
    
    if not user_found:
        data.append([username, str(score)])

    data.sort(key=lambda x: int(x[1]), reverse=False)
    with open(leaderboard_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

def print_leaderboard():
    leaderboard_file = "leaderboard.csv"
    print("Username\tScore")
    with open(leaderboard_file, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print("\t\t".join(row))

def get_guess():
    guess = input("\nEnter a five letter word:").upper()
    while not is_valid_word(guess):
        guess = input("Invalid word! Enter another 5 letter word:").upper()
    return guess

board = [[" " for _ in range(5)] for _ in range(6)]
possible_answers = get_word_array("possibleAnswers.csv")
valid_words = get_word_array("validWords.csv")
answer = possible_answers[random.randint(0, len(possible_answers) - 1)]
main()