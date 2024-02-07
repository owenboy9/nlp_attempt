import spacy
import random
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# load eng language model
nlp = spacy.load("en_core_web_lg")
# import text from file
text = open('text.txt', 'r', encoding='utf8').read()
# convert text to nlp
doc = nlp(text)


def parts(text):
# process  text with spacy
# list pos to exclude

    exclude_pos = {"SPACE", "PUNCT", "X", "SYM", "PART", "AUX", "DET", "PROPN", "NUM"}

#     # empty dictionary to store words grouped by pos
    pos_groups = {}
#
#     # iterate over tokens in doc
    for token in doc:
#         # if token a valid pos and not one of the unwelcome ones
        if token.pos_ not in exclude_pos:
#             # lemmatize it, strip and convert it to lowercase
            lemma = token.lemma_.lower().strip()
#             # add lemma to its pos group: set pos name as default key, if not yet a value, set value to an empty set
            pos_groups.setdefault(token.pos_, set()).add(lemma)
#
#     # convert sets to lists (easier to deal with), iterating through key-value pairs in pos_groups dictionary
    pos_groups = {pos: list(words) for pos, words in pos_groups.items()}
#
    return pos_groups