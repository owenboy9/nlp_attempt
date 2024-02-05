# import spacy and the large version of the english dictionary
import spacy
nlp = spacy.load("en_core_web_lg")
# import features responsible for filtering out stop words and puntuation
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
# import the feature that allows word search
from spacy.matcher import PhraseMatcher

# import reference material
text = open('text.txt', 'r', encoding='utf8').read()

# convert reference material into an nlp document
doc = nlp(text)

# create a function process reference material, turning it into a list of bare words, lower case, lemmatized
def preprocess_text(text):
    # replace newline characters with a space
    text = text.replace('\n', ' ')
    doc = nlp(text)
    # create an empty list to add prepped words to
    words = []
    # extract lemmatized tokens: no stop words, punctuation nor numbers
    tokens = [token.lemma_ for token in doc if token.is_alpha and token.is_stop and not token.is_punct]
    # add stripped and lower-cased words to the list
    for token in tokens:
        bare = token.lower().strip()
        if bare not in words:
            words.append(bare)
    return words
