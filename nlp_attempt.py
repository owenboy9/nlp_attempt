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

# convert reference material into an nlp document
doc = nlp(text)

# function for grouping words by parts of speech, using the prepped word list
def parts(text):
    # instantiate text as nlp doc
    doc = nlp(text)

    # create a dictionary to store words grouped by parts of speech
    pos_groups = {}

    for token in doc:
        # check if token has a valid POS
        if token.pos_:
            # get the part of speech of the token
            pos = token.pos_

            # use the words without additional processing
            bare = token.text
            # tokens = [token.lemma_ for token in doc if token.is_alpha and token.is_stop and not token.is_punct]

            # if pos doesn't already exist in the dictionary, create its group & add token to it
            if pos not in pos_groups:
                pos_groups[pos] = [bare]
            # otherwise, add it
            else:
                pos_groups[pos].append(bare)
    # return the pos dictionary w/pos groups & tag subgroups
    return pos_groups

pos_groups = parts(text)

# lemmatize tokens in pos dictionary by making a new one
lemmatized_pos_groups = {}
# iterate through every item (word) in pos, recreating the first dictionary structure
for pos, words in pos_groups.items():
    # but lemmatizing every word (i.e. also performing .strip())
    lemmatized_pos_groups[pos] = {nlp(word.lower())[0].lemma_ for word in words}

# in order to print the resulting lemmatized dictionary, convert sets to lists
for pos, words in lemmatized_pos_groups.items():
    lemmatized_pos_groups[pos] = list(words)

# list undesired pos
exclude_pos = ["SPACE", "PUNCT", "OTHER", "SYM", "PART", "AUX", "DET", "PROPN", "NUM"]

# filter out undesired POS
final_pos_groups = {pos: words for pos, words in lemmatized_pos_groups.items() if pos not in exclude_pos}

# print the whole thing with explanations
for pos, words in final_pos_groups.items():
    print(f"{spacy.explain(pos)}: {words}\n")