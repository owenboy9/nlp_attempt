import spacy
import random
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# load eng language model
nlp = spacy.load("en_core_web_lg")

# sort words by pos & deliver them pristine and neat (lemmatized, stripped, lower-cased)
def parts(text):
    # process  text with spacy
    doc = nlp(text)

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