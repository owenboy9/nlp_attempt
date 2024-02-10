import os
import spacy
# import the relevant function to be called in the menu
from word_by_word import one_word
# load eng lang model
nlp = spacy.load("en_core_web_lg")


def menu():

    # initiate loop with easy break option
    run = True
    while run:
        # clear the console making sure the code can run on either windows or unix
        os.system('cls' if os.name == 'nt' else 'clear')
        print('welcome to this simple hybrid of a dadaist poet and a pythia\n')
        print('choose your words carefully, one by one, typing in numbers from 1 to 8:\n')
        print("1. adjective\n2. noun\n3. pronoun\n4. verb\n5. adposition\n6. adverb\n7. interjection\n8. conjunction\n")
        # make sure user input is an int & prevent program from crashing
        try:
            # user input for pos
            pos = int(input('1 - 2 - 3 - 4 - 5 - 6 - 7 - 8\n'))
            # make sure user input is within available options
            if 0 < pos <= 8:
                if pos == 1:
                    pos_input = 'ADJ'
                    one = one_word(pos_input)
                elif pos == 2:
                    pos_input = 'NOUN'
                    one = one_word(pos_input)
                elif pos == 3:
                    pos_input = 'PRON'
                    one = one_word(pos_input)
                elif pos == 4:
                    pos_input = 'VERB'
                    one = one_word(pos_input)
                elif pos == 5:
                    pos_input = 'CCONJ'
                    one = one_word(pos_input)
                elif pos == 6:
                    pos_input = 'ADV'
                    one = one_word(pos_input)
                elif pos == 7:
                    pos_input = 'INTJ'
                    one = one_word(pos_input)
                else:
                    pos_input = 'ADJ'
                    one = one_word(pos_input)

                go_on = input("\nDo you want to choose more words? (y/n): ").lower()
                if go_on != 'y':
                    break
            else:
                print("Invalid input. Please enter a number between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a number.")