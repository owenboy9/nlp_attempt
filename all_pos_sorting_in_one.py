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

def sort_and_save():
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
            # filter out stubborn rubbish
            if '--' or '-' or '\'' or '!' or '\"' not in token.text:
                # convert 'SCONJ' to 'CCONJ' to eliminate unnecessary distinction
                if pos == 'SCONJ':
                    pos = 'CCONJ'
                # if a specific word's pos is not yet in the dictionary
                if pos not in pos_lists:
                    # create an empty list for the pos
                    pos_lists[pos] = []
                # add lemma to the list for the pos if it's not already present
                if token.lemma_.lower().strip() not in pos_lists[pos]:
                    pos_lists[pos].append(token.lemma_.lower().strip())
    return pos_lists