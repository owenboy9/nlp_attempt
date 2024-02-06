import spacy
import nlp_attempt
import random
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# load eng language model
nlp = spacy.load("en_core_web_lg")
# import text from text doc
text = open('text.txt', 'r', encoding='utf8').read()

doc = nlp(text)


def start_menu():
    run = True
    selected_words = {}  # Create an empty dictionary to store selected words
    while run:
        answer = input("\nwelcome to your word-spitting machine"
                       "\nchoose your words carefully:"
                       "\n1. pronouns"
                       "\n2. nouns"
                       "\n3. adpositions"
                       "\n4. conjunctions"
                       "\n5. adjectives"
                       "\n6. adverbs"
                       "\n7. verbs"
                       "\n8 interjections"
                       "\nQ quit"
                       "\n-->\n").strip()
        match answer.lower():
            case "1":
                selected_words['pronouns'] = nlp_attempt.pron()  # Store selected pronouns
                run = False
            case "2":
                selected_words['nouns'] = nlp_attempt.nouns()  # Store selected nouns
                run = False
            case "3":
                selected_words['adpositions'] = nlp_attempt.adps()  # Store selected adpositions
                run = False
            case "4":
                selected_words['conjunctions'] = nlp_attempt.conj()  # Store selected conjunctions
                run = False
            case "5":
                selected_words['adjectives'] = nlp_attempt.adjectives()  # Store selected adjectives
                run = False
            case "6":
                selected_words['adverbs'] = nlp_attempt.adverbs()  # Store selected adverbs
                run = False
            case "7":
                selected_words['verbs'] = nlp_attempt.verbs()  # Store selected verbs
                run = False
            case "8":
                selected_words['interjections'] = nlp_attempt.interjections()  # Store selected interjections
                run = False
            case "Q":
                run = False
            case _:
                print(f"{answer} is not a valid option. choose either 1-8 or Q.")

    return selected_words  # Return the dictionary containing all selected words

def print_selected_words(selected_words):
    for pos, words in selected_words.items():
        print(f"{pos}: {words}")

# Call the start_menu function to get the selected words
selected_words = start_menu()

# Print the selected words
print_selected_words(selected_words)