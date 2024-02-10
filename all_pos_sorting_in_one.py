import spacy
import os
# import punctuation detector
from string import punctuation
# load eng language model
nlp = spacy.load("en_core_web_lg")
# import text from file
text = open('text.txt', 'r', encoding='utf8').read()
# convert text to nlp
doc = nlp(text)

# define pos_lists as a global variable
pos_lists = {}

def sort_and_safe():
    global pos_lists  # dictionary to store lists for each pos
    # list punctuation marks and newlines to exclude from text
    skip_words = list(punctuation) + ['\n']
    # list pos to exclude
    exclude_pos = {"SPACE", "PUNCT", "X", "SYM", "PART", "AUX", "DET", "PROPN", "NUM"}
    # run through the text word by word
    for token in doc:
        # simple abbreviation
        pos = token.pos_
        # target the words we do want to deal with
        if token.text not in skip_words and pos not in exclude_pos:
            # if a specific word's pos is not yet in the dictionary
            if pos not in pos_files:
                # use set() to ensure nothing will be duplicated in pos_files dictionary
                pos_files[pos] = set()
                # create new file if it doesn't exist yet naming it after the relevant pos tag
                file_name = f"{pos}_words.txt"
                # standard python module os.path.exists() checks if file_name exists in file system (tracking its path)
                if not os.path.exists(file_name):
                    # if it doesn't, open/create a new one, write mode, and close it right away (standard procedure)
                    open(file_name, 'w').close()
            # open file in read mode ("r") to check if word is already present
            with open(f"{pos}_words.txt", "r") as file:
                # if word not already in it
                if token.lemma_.lower().strip() not in file.read():
                    # open file in append mode ("a") to avoid overwriting existing content
                    with open(f"{pos}_words.txt", "a") as file_append:
                        # & add word to it
                        file_append.write(f"{token.lemma_.lower().strip()}\n")
                    # add word to set to track uniqueness
                    pos_files[pos].add(token.lemma_.lower().strip())