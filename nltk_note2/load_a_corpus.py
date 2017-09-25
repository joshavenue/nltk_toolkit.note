import nltk
from nltk.corpus import PlaintextCorpusReader

corpus_root = '/Users/ypyap/Desktop/untitled folder'

wordlists = PlaintextCorpusReader(corpus_root, 'sample_text.txt')

print(wordlists.fileids())
print(wordlists.raw('sample_text.txt'))