import spacy

nlp = spacy.load("song.spacy")
doc = nlp("I’m 100% down and waiting for Crunk to have its crown back on mainstream. Songs like “Goodies” by Ciara and “Yeah” by Usher still hold a huge spot in my heart.")
doc2 = nlp("Beyoncé - Grown Woman is the main one that comes to mind.")
doc3 = nlp("Luke Chiang's Paragraphs")


for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
for ent in doc2.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
for ent in doc3.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
