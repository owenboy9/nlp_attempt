import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# Load English language model
nlp = spacy.load("en_core_web_lg")


def parts(text):
    # Process the text with spaCy
    doc = nlp(text)

    # Define parts of speech to exclude
    exclude_pos = {"SPACE", "PUNCT", "X", "SYM", "PART", "AUX", "DET", "PROPN", "NUM"}

    # Create a dictionary to store words grouped by parts of speech
    pos_groups = {}

    # Iterate over tokens in the document
    for token in doc:
        # Check if token is not in the exclusion set and has a valid part of speech
        if token.pos_ not in exclude_pos:
            # Lemmatize the token and convert it to lowercase
            lemma = token.lemma_.lower().strip()
            # Add the lemma to the corresponding part of speech group in the dictionary
            pos_groups.setdefault(token.pos_, set()).add(lemma)

    # Convert sets to lists for easier handling
    pos_groups = {pos: list(words) for pos, words in pos_groups.items()}

    return pos_groups


# Example usage
text = open('text.txt', 'r', encoding='utf8').read()
pos_groups = parts(text)

# Print the resulting dictionary
for pos, words in pos_groups.items():
    print(f"{pos}: {words}\n")
