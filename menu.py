import os
import spacy
# import the relevant function to be called in the menu
from word_by_word import one_word
from all_pos_sorting_in_one import pos_lists, sort_and_save
# load eng lang model
nlp = spacy.load("en_core_web_lg")


def menu():
    # empty list to store the words in
    poem = []
    # display list of options
    print('_' * 50)
    print('\nwelcome to this simple hybrid of a dadaist poet and a pythia\n')
    print('choose your words carefully, one by one, by typing in numbers from 1 to 8:\n')
    print('1. adjective\n2. noun\n3. pronoun\n4. verb\n5. adposition\n6. adverb\n7. interjection\n8. conjunction\n')
    print('press enter twice for newline\n')
    # exit option
    print('to exit press Q\n')
    print('_' * 50)
    # initiate loop with easy break option
    while True:
        # clear the console making sure the code can run on either windows or unix
        os.system('cls' if os.name == 'nt' else 'clear')

        # space for user input for pos
        user_input = input()

        # exit option
        if user_input.lower() == 'q':
            break
        # newline option
        elif user_input == '':
            poem.append(f'\n')

        # make sure user input for pos is an int & prevent program from crashing
        try:
            pos = int(user_input)
            # make sure user input is within available options
            if 0 < pos <= 8:
                # convert user input into pos
                pos_input = convert_number_to_pos(pos)

                # call function to get random word from the specific pos list
                one = one_word(pos_input)

                # add word to poem
                poem.append(one)
                spythia = ' '.join(word for word in poem)
                print('_' * 50)
                print(f'\nthis is what you have so far:\n\n{spythia}\n')
                print('_' * 50)
                print('\n1. adjective\n2. noun\n3. pronoun\n4. verb\n5. adposition\n6. adverb\n7. interjection\n8. conjunction\n')
                print('press enter twice for newline\n')
                print('_' * 50)
            else:
                print('numbers from 1 to 8 or double enter please')
        except ValueError:
            print("invalid input. please enter a number.")

    return poem


# function to convert number to part of speech for one_word() to use
def convert_number_to_pos(number):
    if number == 1:
        return 'ADJ'
    elif number == 2:
        return 'NOUN'
    elif number == 3:
        return 'PRON'
    elif number == 4:
        return 'VERB'
    elif number == 5:
        return 'ADP'
    elif number == 6:
        return 'ADV'
    elif number == 7:
        return 'INTJ'
    elif number == 8:
        return 'CONJ'