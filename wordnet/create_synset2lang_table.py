from nltk.corpus import wordnet as wn

def synset_to_str(synset, lang):
    return '|'.join([ l.name() for l in synset.lemmas(lang) ])

def print_synset(synset,langs):
    name = synset.name()
    examples = '|'.join(synset.examples())
    d = synset.definition()
    print('\t'.join([name, '\t'.join([synset_to_str(synset, l) for l in langs]), examples, d]))

# http://www.loc.gov/standards/iso639-2/php/code_list.php
# two languages not found: zsm, qcn

langs2 = ['en',  'sq',  'ar',  'bg',  'ca',  'zh',  'da',  'el' , 'eu',  'fa',  'fi',  'fr',  'gl',  'he',  'hr',  'id',  'it',  'jp',  'nl',  'nn',  'nb',  'pl',  'pt',  'qc',  'sl',  'es',  'sv',  'th', 'ms']
langs3 = ['eng', 'als', 'arb', 'bul', 'cat', 'cmn', 'dan', 'ell', 'eus', 'fas', 'fin', 'fra', 'glg', 'heb', 'hrv', 'ind', 'ita', 'jpn', 'nld', 'nno', 'nob', 'pol', 'por', 'qcn', 'slv', 'spa', 'swe', 'tha', 'zsm']

langs = wn.langs()

print('\t'.join(['synset', '\t'.join(langs2), 'examples', 'definitions']))
for s in wn.all_synsets():
    print_synset(s, langs)

    
