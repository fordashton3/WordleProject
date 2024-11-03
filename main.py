import random
from colorama import init, Fore, Style


def main():

    while isPlaying(): # TODO main gameplay loop
       printBoard(board)

def isPlaying(): # TODO - return true if still playing, false if player won or lost
    if board[6[0]] != "":
        return False
    elif answer == guess


def isValidWord(word): # TODO - return true if player input is a valid guess (use possible_answers array), otherwise false
    for i in possible_answers:
        if word == possible_answers[i]:
            return True
    return False

def printBoard(board):
    for word in board:
        print("----------------\n")
        for i in len(word):
            print("| {} ", end="").format(formatLetter(word, i)) # TODO - implement color for each letter
        print("|")
    print("----------------")

def formatLetter(word, letter_index): # Done, needs testing
    # Green if letter same position as answer
    if word.index(letter_index) == answer.index(letter_index):
        return Fore.GREEN + word.index(letter_index) + Style.RESET_ALL

    # Yellow if letter is in answer
    for i in range(5):
        if word.index(letter_index) == answer.index(i):
            return Fore.YELLOW + word.index(letter_index) + Style.RESET_ALL

    # Dim if letter not in answer
    return Style.DIM + word.index(letter_index) + Style.RESET_ALL

def get_word_array(input_file): # Done, needs testing
    with open(input_file, 'r') as infile:
        words = infile.read().strip().split(',')

        five_letter_words = [word.strip().upper() for word in words if len(word.strip()) == 5]
        return five_letter_words


board = [["" for _ in range(5)] for _ in range(6)]
possible_answers = get_word_array("possibleAnswers.csv")
valid_words = get_word_array("validWords.csv")
answer = possible_answers[random.randint(0, len(possible_answers) - 1)]
guess = ""
main()
