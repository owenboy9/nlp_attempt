import spacy
# load eng language model
nlp = spacy.load("en_core_web_lg")
# import relevant function
import word_by_word
import all_pos_sorting_in_one
# import text from file
text = open('text.txt', 'r', encoding='utf8').read()
# convert text to nlp
doc = nlp(text)


# call w_b_w functions one by one for as long as user pleases, return poem afterwards
def piano():
    # create an empty array for piano poem
    melody = []



# perform adapted basic_functions ONCE AT THE BEGINNING & STORE TEMP RESULTS IN THE PROGRAM ITSELF
# add random order option for user to specify number of words: total OR per category
# add newline and tab
# print out what you already have
# at the end, asses sentimental value and write into a text file, adapt prep_aux_files function for it



