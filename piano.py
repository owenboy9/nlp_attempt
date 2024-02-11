import spacy
import os
# set TERM environment variable because otherwise it's ugly
os.environ['TERM'] = 'xterm-256color'
# load eng language model
nlp = spacy.load("en_core_web_lg")
# import relevant function
from menu import menu
from all_pos_sorting_in_one import sort_and_save
# import text from file
text = open('text.txt', 'r', encoding='utf8').read()
# convert text to nlp
doc = nlp(text)


def piano():
    # call sort_and_save from all_pos_sorting_in_one to create a pos list dictionary
    pos_lists = sort_and_save()
    # capture poem returned by menu()
    final_composition = menu()
    print('here\'s what you have played:\n')
    print(' '.join(final_composition))


# at the end, asses sentimental value and write into a text file, adapt prep_aux_files function for that purpose