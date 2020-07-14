import numpy as np
from nltk.corpus import wordnet as wn

# http://www.loc.gov/standards/iso639-2/php/code_list.php
# two languages not found: zsm, qcn

langs2 = ['en',  'sq',  'ar',  'bg',  'ca',  'zh',  'da',  'el' , 'eu',  'fa',  'fi',  'fr',  'gl',  'he',  'hr',  'id',  'it',  'jp',  'nl',  'nn',  'nb',  'pl',  'pt',  'qc',  'sl',  'es',  'sv',  'th', 'ms']
langs3 = ['eng', 'als', 'arb', 'bul', 'cat', 'cmn', 'dan', 'ell', 'eus', 'fas', 'fin', 'fra', 'glg', 'heb', 'hrv', 'ind', 'ita', 'jpn', 'nld', 'nno', 'nob', 'pol', 'por', 'qcn', 'slv', 'spa', 'swe', 'tha', 'zsm']

langs3_to_langs2 = {}
for l2,l3 in zip(langs2,langs3):
    langs3_to_langs2[l3] = l2

# assert all([l3 == l for l3,l in zip(langs3,wn.langs())]), 'need to update langs2 and langs3'

for s in wn.all_synsets():
    for lang in wn.langs():
        lang2 = lang
        if lang in langs3_to_langs2:
            lang2 = langs3_to_langs2[lang]
        for l in s.lemmas(lang):
            for d in l.derivationally_related_forms():
                print('\t'.join([str(l), l.name(), 'derivationally_related_form', str(d), d.name(), lang2]))

            for p in l.pertainyms():
                print('\t'.join([str(l), l.name(), 'pertainym', str(d), d.name(), lang2]))

            for a in l.antonyms():
                print('\t'.join([str(l), l.name(), 'antonym', str(a), a.name(), lang2]))

for s in wn.all_synsets():
    for lang in wn.langs():
        lang2 = lang
        if lang in langs3_to_langs2:
            lang2 = langs3_to_langs2[lang]
        l = s.lemmas(lang)
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                print('\t'.join([str(l[i]), l[i].name(), 'synonym', str(l[j]), l[j].name(), lang2]))

