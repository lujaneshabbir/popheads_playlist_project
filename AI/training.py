import spacy
import random
import warnings
from training_data.Song_db import data as song_data
from spacy.util import minibatch, compounding
from spacy.training.example import Example

SONGS = song_data("SONG");
print(SONGS)

def train_spacy(TD, itns):
    nlp = spacy.blank("en")
    nlp.add_pipe("ner", name="song_ner")
    nlp.get_pipe("song_ner").add_label("SONG")

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "song_ner"]

    with nlp.disable_pipes(*other_pipes):
        warnings.filterwarnings("once", category=UserWarning, module='spacy')
        optimizer = nlp.begin_training()
        sizes = compounding(4, 32.0, 1.001)
        for itn in range(itns):
            print(f"Starting iteration {str(itn)}")
            random.shuffle(TD)
            losses = {}
            batches = minibatch(TD, sizes)
            for batch in batches:
                for text, annotations in batch:
                    # create Example
                    doc = nlp.make_doc(text)
                    example = Example.from_dict(doc, annotations)
                    # Update the model
                    nlp.update([example], losses=losses, drop=0.3)
            #     nlp.update( batch,
            #                 drop = 0.2,
            #                 sgd=optimizer,
            #                 losses=losses
            #     )
                print(losses)
    return (nlp)

random.shuffle(SONGS)
trained = train_spacy(SONGS, 5)
trained.to_disk("song.spacy")

doc = trained("Beyoncé - Grown Woman is the main one that comes to mind.")

for ent in doc.ents:
    print(ent.text, ent.label)
