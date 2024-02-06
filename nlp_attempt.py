import spacy
import random
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# load eng language model
nlp = spacy.load("en_core_web_lg")
text = open('text.txt', 'r', encoding='utf8').read()
# sort words by pos & deliver them pristine and neat (lemmatized, stripped, lower-cased)
doc = nlp(text)
def adjectives():
    # Initialize an empty list to store adjectives
    adjectives = []
    # Collect all adjectives from the document
    for token in doc:
        if token.pos_ == "ADJ" and token not in adjectives:
            adjectives.append(token.lemma_.lower().strip())
    # Get user input for the number of adjectives desired in the poem
    num_adjectives = int(input('how many adjectives do you want to include in your poem? '))
    # Randomly select the specified number of adjectives from the collected list
    selected_adjectives = random.sample(adjectives, min(num_adjectives, len(adjectives)))
    return selected_adjectives


def nouns():
    nouns = []
    for token in doc:
        if token.pos_ == "NOUN" and token not in nouns:
            nouns.append(token.lemma_.lower().strip())
    num_nouns = int(input('how many nouns do you want to include in your poem? '))

    selected_nouns = random.sample(nouns, min(num_nouns, len(nouns)))
    return selected_nouns

def pron():
    pronouns = []
    for token in doc:
        if token.pos_ == "PRON" and token not in pronouns:
            pronouns.append(token.lemma_.lower().strip())
    num_prons = int(input('how many pronouns do you want to include in your poem? '))

    selected_prons = random.sample(pronouns, min(num_prons, len(pronouns)))
    return selected_prons

def adps():
    adpositions = []
    for token in doc:
        if token.pos_ == "ADP" and token not in adpositions:
            adpositions.append(token.lemma_.lower().strip())
    num_adps = int(input('how many adpositions do you want to include in your poem? '))

    selected_adps = random.sample(adpositions, min(num_adps, len(adpositions)))
    return selected_adps

def conj():
    conjunctions = []
    for token in doc:
        if token.pos_ == "CCONJ" or token.pos_ == "SCONJ" and token not in conjunctions:
            conjunctions.append(token.lemma_.lower().strip())
    num_conjs = int(input('how many conjunctions do you want to include in your poem? '))

    selected_conjs = random.sample(conjunctions, min(num_conjs, len(conjunctions)))
    return selected_conjs

def verbs():
    verbss = []
    for token in doc:
        if token.pos_ == "VERB" and token not in verbss:
            verbss.append(token.lemma_.lower().strip())
    num_verbs = int(input('how many verbs do you want to include in your poem? '))

    selected_verbs = random.sample(verbss, min(num_verbs, len(verbss)))
    return selected_verbs

def adverbs():
    adverbs = []
    for token in doc:
        if token.pos_ == "ADV" and token not in adverbs:
            adverbs.append(token.lemma_.lower().strip())
    num_advs = int(input('how many adverbs do you want to include in your poem? '))

    selected_advs = random.sample(adverbs, min(num_advs, len(adverbs)))
    return selected_advs

def interjections():
    interjections = []
    for token in doc:
        if token.pos_ == "INTJ" and token not in interjections:
            interjections.append(token.lemma_.lower().strip())
    num_intjs = int(input('how many interjections do you want to include in your poem? '))

    selected_intjs = random.sample(interjections, min(num_intjs, len(interjections)))
    return selected_intjs

def parts(text):
    # process  text with spacy
    # list pos to exclude
    exclude_pos = {"SPACE", "PUNCT", "X", "SYM", "PART", "AUX", "DET", "PROPN", "NUM"}

    # empty dictionary to store words grouped by pos
    pos_groups = {}

    # iterate over tokens in doc
    for token in doc:
        # if token a valid pos and not one of the unwelcome ones
        if token.pos_ not in exclude_pos:
            # lemmatize it, strip and convert it to lowercase
            lemma = token.lemma_.lower().strip()
            # add lemma to its pos group: set pos name as default key, if not yet a value, set value to an empty set
            pos_groups.setdefault(token.pos_, set()).add(lemma)

    # convert sets to lists (easier to deal with), iterating through key-value pairs in pos_groups dictionary
    pos_groups = {pos: list(words) for pos, words in pos_groups.items()}

    return pos_groups


pos_groups = parts(text)
# Print the resulting dictionary
for pos in pos_groups.items():
    print(f"{pos}")



# import text from text doc
text = open('text.txt', 'r', encoding='utf8').read()
# run function
pos_groups = parts(text)

num_words_per_pos = 1

# Create a dictionary to store randomly selected words from each POS group
selected_words = {}

# Iterate over each POS group and randomly select words
for pos, words in pos_groups.items():
    selected_words[pos] = random.sample(words, num_words_per_pos)

# Define the desired order of POS
desired_pos_order = ['ADJ', 'NOUN', 'VERB', 'ADV', 'ADP', 'NOUN', 'CONJ', 'PRON', 'VERB', 'ADV']

# Arrange the selected words dictionary based on the desired POS order
arranged_selected_words = {pos: selected_words[pos] for pos in desired_pos_order if pos in selected_words}

# Join the randomly selected words from all POS groups into a single string
random_string = ' '.join([word for words in arranged_selected_words.values() for word in words])

# Print the resulting string
print(random_string)