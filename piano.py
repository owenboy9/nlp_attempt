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
    # call sort_and_save from all_pos_sorting_in_one to create a pos list dictionary
    pos_lists = all_pos_sorting_in_one.sort_and_save()
    run = True
    while run:
        # make sure user input is an int & prevent program from crashing
        try:
            # user input for pos
            pos = int(input('choose your words carefully, one by one:'
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
        # reformat resulting array into a neat line of words
    spitout = ' '.join(word for word in poem)
    return spitout



# perform adapted basic_functions ONCE AT THE BEGINNING & STORE TEMP RESULTS IN THE PROGRAM ITSELF
# add random order option for user to specify number of words: total OR per category
# add newline and tab
# print out what you already have
# at the end, asses sentimental value and write into a text file, adapt prep_aux_files function for it



