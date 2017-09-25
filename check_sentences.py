import nltk
from nltk.corpus import gutenberg

kjv_sentences = gutenberg.sents('bible-kjv.txt')

longest_len = max(len(s) for s in kjv_sentences)

x = [s for s in kjv_sentences if len(s) == kjv_sentences]

print(longest_len)