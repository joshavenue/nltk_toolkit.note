import nltk
from nltk.corpus import gutenberg

print(gutenberg.fileids())

emma = gutenberg.words('austen-emma.txt')

print(emma)

## This is a way to open a library from the source of nltk