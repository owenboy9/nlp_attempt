1. build reference material composed of three classic literary works: mrs dalloway, ulysses, and tender buttons. although the app is supposed to spit out poetry, the literary genre of texts used for reference material does not matter, because the app will pick singular words to build poetry with. like bricks.
2. write a function that will process reference text turning it into a list of "bare" and "relevant" words, that is, no stop words, no punctuation marks, all lower case and lemmatized.
3. create a separate file for the menu(s)
4. cluster words by parts of speech
5. try reverse order: spacy won't do proper .pos on prepped words (lemmatized, stipped, etc.) so i'm trying to divide them into pos groups first, and then clean it all up (set, lemma, strip, etc) and create proper pos lists
6. final filtered and lemmatized pos dicitonary is done. took some time, required rethinking the level of fine-grained searches, and the order in which to proceed. next step should be a simple mix word bag to see how my idea works. user input and menu will have to wait.
7. 

