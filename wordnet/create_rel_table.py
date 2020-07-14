import numpy as np
from nltk.corpus import wordnet as wn

for head in wn.all_synsets():
    for rel in ['hyponyms', 'hypernyms', 'part_meronyms', 'substance_meronyms', 'part_holonyms', 'substance_holonyms', 'entailments']:
        for tail in getattr(head, rel)():
            print('\t'.join([head.name(), rel, tail.name()]))
