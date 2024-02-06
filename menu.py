import spacy
import random
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# load eng language model
nlp = spacy.load("en_core_web_lg")
# import text from text doc
text = open('text.txt', 'r', encoding='utf8').read()