import spacy
import random
# load eng language model
nlp = spacy.load("en_core_web_lg")
#import the relevant function with the global variable dictionary of pos lists
from all_pos_sorting_in_one import pos_lists


# function for picking ONE random word from a pos list: list = user input
def one_word(pos_input):
    # ascribe menu option-based pos to its list
    pos_list = pos_lists[pos_input.upper()]
    # variable to store random.choice()
    one = random.choice(pos_list)
    return one