import spacy
import random
# load eng language model
nlp = spacy.load("en_core_web_lg")


# function for picking ONE random word from a text file: file = user input
def one_word(filename):
    # open file and read its contents
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    # convert text into nlp
    doc = nlp(text)
    # convert nlp doc into an array for random.choice, pick up only the actual words
    words = [token.text for token in doc]
    # variable to store random.choice()
    one = random.choice(words)
    return one

one = one_word('more_text.txt')
print(one)