import spacy
# load eng language model
nlp = spacy.load("en_core_web_lg")
# import relevant function
from menu import menu
import all_pos_sorting_in_one
# import text from file
text = open('text.txt', 'r', encoding='utf8').read()
# convert text to nlp
doc = nlp(text)


# call w_b_w functions one by one for as long as user pleases, return poem afterwards
def piano():
    # call sort_and_save from all_pos_sorting_in_one to create a pos list dictionary
    pos_lists = all_pos_sorting_in_one.sort_and_save()
    menu()



# at the end, asses sentimental value and write into a text file, adapt prep_aux_files function for that purpose



