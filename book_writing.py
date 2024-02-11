import spacy
# import spacy textblob for sentiment analysis
from spacytextblob.spacytextblob import SpacyTextBlob
# will be necessary for creating directories and files
import os
# load lang model
nlp = spacy.load('en_core_web_lg')
# add spacytextblob to pipeline (for text analysis)
nlp.add_pipe('spacytextblob')


# analyze sentiment
def analyze_sentiment(text):
    # nlp text
    doc = nlp(text)
    # access sentiment score using ._.blob.polarity
    polarity = doc._.blob.polarity
    return polarity


def write_poem(poem):
    # analyze sentiment
    polarity = analyze_sentiment(poem)
    # translate polarity score to text description
    if 0 > polarity >= -0.5:
        text_polarity = "can always get gloomier"
    elif polarity < -0.5:
        text_polarity = "bottomless abyss"
    elif 0 < polarity < 0.5:
        text_polarity = "yes"
    elif polarity == 0:
        text_polarity = "oh well"
    else:
        text_polarity = "improbably perky"

    # check if directory for sentiment score exists, if not, create it
    directory = "poems/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # generate file name based on sentiment
    filename = os.path.join(directory, f"{text_polarity}.txt")

    # write poem to the file (open file in append mode ("a") to avoid overwriting existing content)
    with open(filename, "a") as file:
        file.write(poem + "\n\n")