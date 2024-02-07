import spacy
import os
# import punctuation detector
from string import punctuation
# load eng language model
nlp = spacy.load("en_core_web_lg")
# import text from file
text = open('text.txt', 'r', encoding='utf8').read()
# convert text to nlp
doc = nlp(text)

# Define pos_files as a global variable
pos_files = {}

def preprocess_and_write_to_files():
    global pos_files  # Dictionary to store files for each POS tag
    # make a list of punctuation marks and newlines to exclude from the text
    skip_words = list(punctuation) + ['\n']
    # list pos to exclude
    exclude_pos = {"SPACE", "PUNCT", "X", "SYM", "PART", "AUX", "DET", "PROPN", "NUM"}
    # empty tuples to store words grouped by pos before they are sent into their respective text files
    for token in doc:
        pos = token.pos_
        if token.text not in skip_words and pos not in exclude_pos:
            if pos not in pos_files:
                pos_files[pos] = set()  # Use a set to store unique words
                # Create a new file if it doesn't exist
                file_name = f"{pos}_words.txt"
                if not os.path.exists(file_name):
                    open(file_name, 'w').close()
            # Open file in read mode ("r") to check if the word is already present
            with open(f"{pos}_words.txt", "r") as file:
                # Check if the word is already in the file
                if token.lemma_.lower().strip() not in file.read():
                    # Open file in append mode ("a") to avoid overwriting existing content
                    with open(f"{pos}_words.txt", "a") as file_append:
                        file_append.write(f"{token.lemma_.lower().strip()}\n")  # Write word to file
                    # Add word to set to track uniqueness
                    pos_files[pos].add(token.lemma_.lower().strip())




# Delete existing files
# def delete_existing_files():
#     for pos in pos_files:
#         file_name = f"{pos}_words.txt"
#         if os.path.exists(file_name):
#             os.remove(file_name)
#
# # Call the function to delete existing files
# delete_existing_files()


# Example usage
preprocess_and_write_to_files()
#
# # function to sort words by pos and write them directly into txt files it creates in one move
# def preprocess_and_write_to_files():
#     pos_files = {}  # dictionary to store files for each pos
#     # list of punctuation marks and newlines to exclude from text
#     skip_words = list(punctuation) + ['\n']
#     # list pos to exclude
#     exclude_pos = {"SPACE", "PUNCT", "X", "SYM", "PART", "AUX", "DET", "PROPN", "NUM"}
#     # open loop running through the whole text word by word
#     for token in doc:
#         # simple abbreviation
#         pos = token.pos_
#         # narrow search down to words we're interested in
#         if token.text not in skip_words and pos not in exclude_pos:
#             # make sure pos files won't be repeated in their dict
#             if pos not in pos_files:
#                 # CREATE TEXT FILE TO WRITE ITS POS INTO (write mode, "w")
#                 pos_files[pos] = open(f"{pos}_words.txt", "w")
#             # open/instantiate file in read mode ("r"), check if word (in its most stripped form) already in it
#             with open(f"{pos}_words.txt", "r") as file:
#                 if token.lemma_.lower().strip() not in file.read():
#                     # write word to file, newline after every one
#                     pos_files[pos].write(f"{token.lemma_.lower().strip()}\n")
#     # close all files when filled
#     for file in pos_files.values():
#         file.close()
#
# # Example usage
# preprocess_and_write_to_files()
