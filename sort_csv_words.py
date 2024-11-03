import nltk
from nltk.corpus import words


def save_five_letter_words(output_file):
    # Fetch the list of English words
    word_list = words.words()

    # Filter for 5-letter words
    five_letter_words = [word for word in word_list if len(word) == 5]

    # Write the words to the output file, separated by commas
    with open(output_file, 'w') as outfile:
        outfile.write(','.join(five_letter_words))


if __name__ == "__main__":
    output_file = 'validWords.csv'
    save_five_letter_words(output_file)
    print(f"Saved 5-letter words to {output_file}.")
