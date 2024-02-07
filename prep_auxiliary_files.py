import spacy
# import punctuation detector
from string import punctuation
# load eng language model
nlp = spacy.load("en_core_web_lg")
# import text from file
text = open('text.txt', 'r', encoding='utf8').read()
# convert text to nlp
doc = nlp(text)


def preprocess_and_write_to_files():
    pos_files = {}  # Dictionary to store files for each POS tag
    # make a list of punctuation marks and newlines to exclude from the text
    skip_words = list(punctuation) + ['\n']
    # list pos to exclude
    exclude_pos = {"SPACE", "PUNCT", "X", "SYM", "PART", "AUX", "DET", "PROPN", "NUM"}
    # empty tuples to store words grouped by pos before they are sent into their respective text files
    for token in doc:
        pos = token.pos_
        if token.text not in skip_words and pos not in exclude_pos:
            if pos not in pos_files:
                pos_files[pos] = open(f"{pos}_words.txt", "w")
            # Open file in read mode ("r") to check if the token is already in the file
            with open(f"{pos}_words.txt", "r") as file:
                if token.lemma_.lower().strip() not in file.read():
                    # Write word to file
                    pos_files[pos].write(f"{token.lemma_.lower().strip()}\n")
    # Close all files after writing to them
    for file in pos_files.values():
        file.close()

# Example usage
preprocess_and_write_to_files()
