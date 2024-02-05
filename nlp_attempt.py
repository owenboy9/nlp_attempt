#import spacy and the large version of the english dictionary
import spacy
nlp = spacy.load("en_core_web_lg")
#import features responsible for filtering out stop words and puntuation
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
#import the feature that allows word search
from spacy.matcher import PhraseMatcher


#create a list of elements to cut out of reference material material
# skip_words = list(STOP_WORDS) + list(punctuation) + ['\n']

#import reference material
text = open('text.txt', 'r', encoding='utf8').read()

#convert reference material into an nlp document
doc = nlp(text)

#create a list of words to work with
# all_words = [word.text for word in doc]

#create a function process reference material, turning it into a list of bare words, lower case, lemmatized
def preprocess_text(text):
    # replace newline characters with a space
    text = text.replace('\n', ' ')
    doc = nlp(text)
    #create an empty list to add prepped words to
    words = []
    # extract lemmatized tokens without stop words and punctuation
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    #
    for token in tokens:
        bare = token.lower().strip()
        if bare not in words:
            words.append(bare)

    print(words)

preprocess_text(text)