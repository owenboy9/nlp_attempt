import spacy
import random
# load eng language model
nlp = spacy.load("en_core_web_lg")
# import text from file
text = open('text.txt', 'r', encoding='utf8').read()
# convert text to nlp
doc = nlp(text)

# call w_b_w functions one by one for as long as user pleases, return poem afterwards
# add newline and tab options