# -*- coding: utf-8 -*-

import treetaggerwrapper as ttw
import settings

tagger = ttw.TreeTagger(TAGLANG='en', TAGDIR=settings.TTBin)
tags = tagger.tag_file("PIERC18111901.txt")
tags = ttw.make_tags(tags)

print(tags)
NN_list = ["NN", "NNS", "NP", "NPS"]
nns = [tag.lemma for tag in tags if tag.pos in NN_list]
print(nns)
