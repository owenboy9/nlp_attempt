import spacy

nlp = spacy.load("en_core_web_lg")

# import text from file
text = open('../text.txt', 'r', encoding='utf8').read()

# process text with spacy
doc = nlp(text)
nlp.add_pipe(Language())

