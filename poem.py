import spacy
import random
import numpy
# import pos functions from basic_functions
from basic_functions import adjectives
from basic_functions import nouns
from basic_functions import pron
from basic_functions import verbs
from basic_functions import adps
from basic_functions import interjections
from basic_functions import conj
from basic_functions import adverbs

# load eng lang model
nlp = spacy.load("en_core_web_lg")

# import text from file
text = open('text.txt', 'r', encoding='utf8').read()

# process text with spaCy
doc = nlp(text)
# function: user input = desired number of words from each of the pos groups that are made available,
# output: a verse generated out of words randomly picked, within each pos category, from text
def dyi_poem():
    # empty tuple to store the words in
    poem = []
    # initiate loop with easy break option
    run = True
    while run:
        # make sure user input is an int & prevent program from crashing
        try:
            # user input for pos
            pos = int(input('choose your parts of speech:'
                                '\n1. adjective\n2. noun\n3. pronoun\n'
                                '4. verb\n5. adposition\n6. adverb\n7. interjection\n8. conjunction\n'))
            # make sure user input is within available options
            if 0 < pos <= 8:
                if pos == 1:
                    # call pos function, add each item to poem (extend(); not append() --> returns one word/pos)
                    poem.extend(adjectives())
                    # let user decide whether they need more words
                    go_on = input('need more words? y/n\n')
                    if go_on == 'y':
                        # return to main pos menu, keep choosing
                        continue
                    elif go_on == 'n':
                        # exit loop, go straight to return
                        run = False
                    else:
                        print('invalid input')
                        continue
                elif pos == 2:
                    poem.extend(nouns())
                    go_on = input('need more words? y/n\n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                    continue
                elif pos == 3:
                    poem.extend(pron())
                    go_on = input('need more words? y/n\n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                    continue
                elif pos == 4:
                    poem.extend(verbs())
                    go_on = input('need more words? y/n\n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                    continue
                elif pos == 5:
                    poem.extend(adps())
                    go_on = input('need more words? y/n\n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                    continue
                elif pos == 6:
                    poem.extend(adverbs())
                    go_on = input('need more words? y/n\n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                    continue
                elif pos == 7:
                    poem.extend(interjections())
                    go_on = input('need more words? y/n\n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                    continue
                else:
                    poem.extend(conj())
                    go_on = input('need more words? y/n\n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                    continue
        except ValueError:
            # prevent program from crashing if invalid input
            print('invalid input')
        # reformat resulting tupple into a neat sentence
    spitout = ' '.join(word for word in poem)
    return spitout

# run function
spitout = dyi_poem()

print('_' * 50)
print(f'here\'s your poem:\n {spitout}')
print('_' * 50)