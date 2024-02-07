import spacy
import random
import numpy
from basic_functions import adjectives
from basic_functions import nouns
from basic_functions import pron
from basic_functions import verbs
from basic_functions import adps
from basic_functions import interjections
from basic_functions import conj
from basic_functions import adverbs

# load English language model
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
            # make sure user input is correct
            if 0 < pos <= 8:
                #/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
                if pos == 1:
                    poem.append(adjectives())
                    go_on = input('need more words? y/n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                        continue
                elif pos == 2:
                    poem.append(nouns())
                    go_on = input('need more words? y/n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                    continue
                elif pos == 3:
                    poem.append(pron())
                    go_on = input('need more words? y/n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                    continue
                elif pos == 4:
                    poem.append(verbs())
                    go_on = input('need more words? y/n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                    continue
                elif pos == 5:
                    poem.append(adps())
                    go_on = input('need more words? y/n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                    continue
                elif pos == 6:
                    poem.append(adverbs())
                    go_on = input('need more words? y/n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                    continue
                elif pos == 7:
                    poem.append(interjections())
                    go_on = input('need more words? y/n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                    continue
                else:
                    poem.append(conj())
                    go_on = input('need more words? y/n')
                    if go_on == 'y':
                        continue
                    elif go_on == 'n':
                        run = False
                    else:
                        print('invalid input')
                    continue
        except ValueError:
            print('invalid input')

    spitout = ' '.join(word[0] for word in poem)
    return spitout

spitout = dyi_poem()
print(spitout)