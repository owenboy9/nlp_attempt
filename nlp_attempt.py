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

# create a function process reference material, turning it into a list of bare words, lower case, lemmatized


# function for grouping words by parts of speech, using the prepped word list
def parts(text):
    # instantiate bare word list as nlp doc
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
pos_groups = parts(bare_words)
for pos, words in pos_groups.items():
    print(f"{pos}: {words}")

def preprocess_text(text):
    # replace newline characters with a space
    text = text.replace('\n', ' ')
    doc = nlp(text)
    # create an empty list to add prepped words to
    words = []
    # extract lemmatized tokens: no stop words, punctuation nor numbers
    tokens = [token.lemma_ for token in doc if token.is_alpha and token.is_stop and not token.is_punct]
    # add stripped and lower-cased words to the list, prevent repetitions
    for token in tokens:
        bare = token.lower().strip()
        if bare not in words:
            words.append(bare)
    return words

bare_words = preprocess_text(text)