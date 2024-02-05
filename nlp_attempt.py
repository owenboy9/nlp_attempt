# import spacy and the large version of the english dictionary
import spacy
nlp = spacy.load("en_core_web_lg")
# import features responsible for filtering out stop words and punctuation
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
# import the feature that allows word search
from spacy.matcher import PhraseMatcher

# import reference material
text = open('text.txt', 'r', encoding='utf8').read()

# convert reference material into nlp document
doc = nlp(text)

# function for grouping words by parts of speech, using the prepped word list
def parts(text):
    # instantiate text as nlp doc
    doc = nlp(text)

    # create a dictionary to store words grouped by parts of speech
    pos_groups = {}
    # run through the whole text
    for token in doc:
        # check if token has a valid pos
        if token.pos_:
            # get the part of speech of the token
            pos = token.pos_
            # use the words without additional processing for greater pos accuracy
            bare = token.text
            # create a list of pos to be excluded from final dictionary & use it as first filter
            exclude_pos = ["SPACE", "PUNCT", "X", "SYM", "PART", "AUX", "DET", "PROPN", "NUM"]
            if pos not in exclude_pos:
                # if pos doesn't already exist in dictionary, create its group & add token to it
                if pos not in pos_groups:
                    pos_groups[pos] = [bare]
                # otherwise, add it to existing pos group
                else:
                    pos_groups[pos].append(bare)
    # return the pos dictionary w/pos groups
    return pos_groups

# press play to get the outcome
pos_groups = parts(text)

# lemmatize tokens in pos dictionary by making a new one
lemmatized_pos_groups = {}
# iterate through every item (word) in every pos, recreating the first dictionary's structure
for pos, words in pos_groups.items():
    # but lemmatizing every word (also turning it to lower case and performing .strip() by default)
    lemmatized_pos_groups[pos] = {nlp(word.lower())[0].lemma_ for word in words}

# in order to print the resulting lemmatized dictionary, convert sets to lists
for pos, words in lemmatized_pos_groups.items():
    lemmatized_pos_groups[pos] = list(words)

for pos, words in lemmatized_pos_groups.items():
    print(f"{spacy.explain(pos)}: {words}\n")