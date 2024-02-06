import spacy
import random
import numpy
from nlp_attempt import adjectives
from nlp_attempt import nouns
from nlp_attempt import pron
from nlp_attempt import verbs
from nlp_attempt import adps
from nlp_attempt import interjections
from nlp_attempt import conj
from nlp_attempt import adverbs

# Load English language model
nlp = spacy.load("en_core_web_lg")

# Import text from text file
text = open('text.txt', 'r', encoding='utf8').read()

# Process the text with spaCy
doc = nlp(text)

def dyi_poem():
    poem = []
    run = True
    while run:
        # Get user input for the part of speech (POS)
        try:
            pos = int(input('choose your parts of speech:'
                                '\n1. adjective\n2. noun\n3. pronoun\n'
                                '4. verb\n5. adposition\n6. adverb\n7. interjection\n8. conjunction\n'))
            if 0 < pos <= 8:
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
    print(poem)

dyi_poem()