# Wordnet_tables
Extract WordNet tables from NLTK
<p>
Creates a three simple tables:

<ol>
  <li>synset2lang_table.txt: synset --> glosses in 29 languages + examples & definitions</li>
  <li>rel_table.txt: (head, rel, tail), where head and tail are synsets</li>
  <li>lemma_table.txt: (head, rel, tail, language), where head and tail are lemmas</li>
</ol>

Code is embarrassingly simple.
<p>
Depends on NLTL (please install that first; see https://www.nltk.org/install.html)

<p>
Usage:

python3 create_lemma_table.py > lemma_table.txt
<br>
python3 create_rel_table.py > rel_table.txt
<br>
python3 create_synset2lang_table.py > synset2lang_table.txt

echo 'This is a test of morphological decompositions of some words' | tr ' ' '\n' | python3 wordnet_decomp.py 
