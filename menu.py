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
                nlp_attempt.pron()
                run = False
            case "2":
                nlp_attempt.nouns()
                run = False
            case "3":
                nlp_attempt.adps()
                run = False
            case "4":
                nlp_attempt.conj()
                run = False
            case "5":
                nlp_attempt.adjectives()
                run = False
            case "6":
                nlp_attempt.adverbs()
                run = False
            case "7":
                nlp_attempt.verbs()
                run = False
            case "8":
                nlp_attempt.interjections()
                run = False
            case "Q":
                run = False
            case _:
                print(f"{answer} is not a valid option. choose either 1-8 or Q.")