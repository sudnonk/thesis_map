# -*- coding: utf-8 -*-

import treetaggerwrapper as ttw

tagger = ttw.TreeTagger(TAGLANG='en', TAGDIR='c:\\TreeTagger')
tags = tagger.tag_file("test.txt")
tags = ttw.make_tags(tags)

print(tags)
NN_list = ["NN", "NNS", "NP", "NPS"]
nns = [tag.lemma for tag in tags if tag.pos in NN_list]
print(nns)
