import spacy
import os
# set TERM environment variable because otherwise it's ugly
os.environ['TERM'] = 'xterm-256color'
# load eng language model
nlp = spacy.load("en_core_web_lg")
# import relevant function
from piano import piano
# import text from file
text = open('text.txt', 'r', encoding='utf8').read()
# convert text to nlp
doc = nlp(text)

#press play
piano()