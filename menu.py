import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

nlp = spacy.load("en_core_web_lg")
text = open('text.txt', 'r', encoding='utf8').read()
doc = nlp(text)

def parts(text):
    doc = nlp(text)

    pos_groups = {}

    for token in doc:
        if token.is_alpha and token.is_stop and not token.is_punct and token.text != '\n':
            pos = token.pos_
            tag = token.tag_
            bare = token.text

            # Ensure each token appears only once in the dictionary
            if pos not in pos_groups:
                pos_groups[pos] = {tag: {bare}}
            elif tag not in pos_groups[pos]:
                pos_groups[pos][tag] = {bare}
            else:
                pos_groups[pos][tag].add(bare)

    return pos_groups

# Example usage
pos_groups = parts(text)

# Print the resulting dictionary
for pos, tags in pos_groups.items():
    print(f"{pos}: {tags}")
