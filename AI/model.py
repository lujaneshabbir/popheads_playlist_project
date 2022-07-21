import spacy

nlp = spacy.load("song.spacy")
doc = nlp("Beyoncé - Grown Woman is the main one that comes to mind.")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
