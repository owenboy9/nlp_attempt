# import spacy and the large version of the english dictionary
import spacy
from spacy.lang.en.tokenizer_exceptions import word

nlp = spacy.load("en_core_web_lg")
# import features responsible for filtering out stop words and punctuation
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# import reference material
text = open('text.txt', 'r', encoding='utf8').read()

# convert reference material into an nlp document
doc = nlp(text)

def parts(text):
    doc = nlp(text)

    # create a dictionary to store words grouped by parts of speech
    pos_groups = {}

    for token in doc:
        # check if token has a valid POS
        if token.pos_:
            # get the part of speech of the token
            pos = token.pos_
            tag = token.tag_  # fine-grained part-of-speech tag

            # use the word from bare_words without additional processing
            bare = token.text

            # add token to its POS group in dictionary
            if pos not in pos_groups:
                pos_groups[pos] = {tag: [bare]}
            else:
                if tag not in pos_groups[pos]:
                    pos_groups[pos][tag] = [bare]
                else:
                    pos_groups[pos][tag].append(bare)

    return pos_groups

# example usage
pos_groups = parts(text)
def bare_words(text):
    bare_words = []
    if word not in bare_words:
        for pos, words in pos_groups.items():
            bare_words.extend({word: words[words]})
    print(bare_words)