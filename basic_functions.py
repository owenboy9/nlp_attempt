import spacy
import random
# load eng language model
nlp = spacy.load("en_core_web_lg")
# import text from file
text = open('text.txt', 'r', encoding='utf8').read()
# convert text to nlp
doc = nlp(text)


# functions choosing specific pos from text: pick as many as user wishes random words within the pos. same pattern everywhere
def adjectives():
    # empty array to store words
    adjectivess = []
    for token in doc:
        # get all adjectives from text, make sure there are no repetitions
        if token.pos_ == "ADJ" and token.text not in adjectivess:
            # stripped and lemmatized, add them to array
            adjectivess.append(token.lemma_.lower().strip())
    # while loop for trying if input is correct
    run = True
    while run:
        # make sure input's an int
        try:
            # get user input for the number of adjectives desired in the poem
            num_adjectives = int(input('how many adjectives do you want to include in your poem? '))
            run = False
        except ValueError:
            # catch invalid input w/o crashing
            print('invalid input try again')
    # shuffle the array to prevent potential repetitions ensuing from number randomization
    random.shuffle(adjectivess)
    # slice the shuffled list to get the desired number of unique adjectives
    selected_adjectives = adjectivess[:min(num_adjectives, len(adjectivess))]
    return selected_adjectives



def nouns():
    nounss = []
    for token in doc:
        if token.pos_ == "NOUN" and token not in nounss:
            nounss.append(token.lemma_.lower().strip())
    run = True
    while run:
        try:
            num_nouns = int(input('how many nouns do you want to include in your poem? '))
            run = False
        except ValueError:
            print('invalid input try again')
    random.shuffle(nounss)
    selected_nouns = nounss[:min(num_nouns, len(nounss))]
    return selected_nouns

def pron():
    pronouns = []
    for token in doc:
        if token.pos_ == "PRON" and token not in pronouns:
            pronouns.append(token.lemma_.lower().strip())
    run = True
    while run:
        try:
            num_prons = int(input('how many pronouns do you want to include in your poem? '))
            run = False
        except ValueError:
            print('invalid input try again')
    random.shuffle(pronouns)
    selected_prons = pronouns[:min(num_prons, len(pronouns))]
    return selected_prons

def adps():
    adpositions = []
    for token in doc:
        if token.pos_ == "ADP" and token not in adpositions:
            adpositions.append(token.lemma_.lower().strip())
    run = True
    while run:
        try:
            num_adps = int(input('how many adpositions do you want to include in your poem? '))
            run = False
        except ValueError:
            print('invalid input try again')
    random.shuffle(adpositions)
    selected_adps = adpositions[:min(num_adps, len(adpositions))]
    return selected_adps

def conj():
    conjunctions = []
    for token in doc:
        if token.pos_ == "CCONJ" or token.pos_ == "SCONJ" and token not in conjunctions:
            conjunctions.append(token.lemma_.lower().strip())
    run = True
    while run:
        try:
            num_conjs = int(input('how many conjunctions do you want to include in your poem? '))
            run = False
        except ValueError:
            print('invalid input try again')
    random.shuffle(conjunctions)
    selected_conjs = conjunctions[:min(num_conjs, len(conjunctions))]
    return selected_conjs

def verbs():
    verbss = []
    for token in doc:
        if token.pos_ == "VERB" and token not in verbss:
            verbss.append(token.lemma_.lower().strip())
    run = True
    while run:
        try:
            num_verbs = int(input('how many verbs do you want to include in your poem? '))
            run = False
        except ValueError:
            print('invalid input try again')
    random.shuffle(verbss)
    selected_verbs = verbss[:min(num_verbs, len(verbss))]
    return selected_verbs

def adverbs():
    adverbss = []
    for token in doc:
        if token.pos_ == "ADV" and token not in adverbss:
            adverbss.append(token.lemma_.lower().strip())
    run = True
    while run:
        try:
            num_advs = int(input('how many adverbs do you want to include in your poem? '))
            run = False
        except ValueError:
            print('invalid input try again')
    random.shuffle(adverbss)
    selected_advs = adverbss[:min(num_advs, len(adverbss))]
    return selected_advs

def interjections():
    interjectionss = []
    for token in doc:
        if token.pos_ == "INTJ" and token not in interjectionss:
            interjectionss.append(token.lemma_.lower().strip())
    run = True
    while run:
        try:
            num_intjs = int(input('how many interjections do you want to include in your poem? '))
            run = False
        except ValueError:
            print('invalid input try again')
    random.shuffle(interjectionss)
    selected_intjs = interjectionss[:min(num_intjs, len(interjectionss))]
    return selected_intjs

# def parts(text):
#     # process  text with spacy
#     # list pos to exclude
#     exclude_pos = {"SPACE", "PUNCT", "X", "SYM", "PART", "AUX", "DET", "PROPN", "NUM"}
#
#     # empty dictionary to store words grouped by pos
#     pos_groups = {}
#
#     # iterate over tokens in doc
#     for token in doc:
#         # if token a valid pos and not one of the unwelcome ones
#         if token.pos_ not in exclude_pos:
#             # lemmatize it, strip and convert it to lowercase
#             lemma = token.lemma_.lower().strip()
#             # add lemma to its pos group: set pos name as default key, if not yet a value, set value to an empty set
#             pos_groups.setdefault(token.pos_, set()).add(lemma)
#
#     # convert sets to lists (easier to deal with), iterating through key-value pairs in pos_groups dictionary
#     pos_groups = {pos: list(words) for pos, words in pos_groups.items()}
#
#     return pos_groups
#
#
# pos_groups = parts(text)
# # Print the resulting dictionary
# for pos in pos_groups.items():
#     print(f"{pos}")
#
#
#
# # import text from text doc
# text = open('text.txt', 'r', encoding='utf8').read()
# # run function
# pos_groups = parts(text)
#
# num_words_per_pos = 1
#
# # Create a dictionary to store randomly selected words from each POS group
# selected_words = {}
#
# # Iterate over each POS group and randomly select words
# for pos, words in pos_groups.items():
#     selected_words[pos] = random.sample(words, num_words_per_pos)
#
# # Define the desired order of POS
# desired_pos_order = ['ADJ', 'NOUN', 'VERB', 'ADV', 'ADP', 'NOUN', 'CONJ', 'PRON', 'VERB', 'ADV']
#
# # Arrange the selected words dictionary based on the desired POS order
# arranged_selected_words = {pos: selected_words[pos] for pos in desired_pos_order if pos in selected_words}
#
# # Join the randomly selected words from all POS groups into a single string
# random_string = ' '.join([word for words in arranged_selected_words.values() for word in words])
#
# # Print the resulting string
# print(random_string)