import numpy as np
from nltk.corpus import wordnet as wn
import sys

for line in sys.stdin:
    for w in line.rstrip().lower().split():
        print('\t'.join([w, str(wn.morphy(w))]))
    


