# Wordnet_tables
Extract WordNet tables from NLTK
<p>
Creates a three simple tables:

<ol>
  <li>synset2lang_table.txt: synset --> glosses in 29 languages + examples & definitions</li>
  <li>rel_table.txt: (head, rel, tail), where head and tail are synsets</li>
  <li>lemma_table.txt: (head, rel, tail, language), where head and tail are lemmas</li>
</ol>

Code is embarrassingly simple.  Requires numpy and NLTK.  Please install that first.
See https://www.nltk.org/install.html for NLTK.
<p>
Then go into python and say:
<br>
import nltk
  <br>
nltk.download('wordnet')
  <br>
  nltk.download('omw')

<p>
Usage:

python3 create_lemma_table.py > lemma_table.txt
<br>
python3 create_rel_table.py > rel_table.txt
<br>
python3 create_synset2lang_table.py > synset2lang_table.txt

echo 'This is a test of morphological decompositions of some words' | tr ' ' '\n' | python3 wordnet_decomp.py 

Questions: kenneth.ward.church@gmail.com
