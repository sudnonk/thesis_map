# -*- coding: utf-8 -*-

import treetaggerwrapper as ttw
import settings
import os
from gensim import models
from gensim.models.doc2vec import Doc2Vec, Doc2VecVocab, TaggedDocument
import itertools

INPUT_DIR = ".\\corpus"
OUTPUT_FILE = ".\\test.model"

NN_list = ["NN", "NNS", "NP", "NPS"]


def get_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield file, os.path.join(root, file)


def split_words(path, doc_id=''):
    tagger = ttw.TreeTagger(TAGLANG='en', TAGDIR=settings.TTBin)

    tags = tagger.tag_file(path)
    tags = ttw.make_tags(tags)

    return TaggedDocument(tags=[doc_id], words=[tag.lemma for tag in tags if tag.pos in NN_list])


def get_sentences(input_dir):
    for name, path in get_all_files(input_dir):
        yield split_words(path, name)


def train(words):
    model = models.Doc2Vec(documents=words, dm=1, vector_size=400, sample=1e-6, window=10, min_count=1, epochs=100,
                           workers=6)

    return model


if __name__ == '__main__':
    sentences = list(get_sentences(INPUT_DIR))
    print(sentences)
    ids = [sentence.tags[0] for sentence in sentences]

    trained_model = train(sentences)
    trained_model.save(OUTPUT_FILE)

    print(ids)
    for items in list(itertools.combinations(ids, 2)):
        print(items[0], items[1], trained_model.docvecs.similarity(items[0], items[1]))
