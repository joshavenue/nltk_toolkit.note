import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_word = ['Apple','Appler','appling','appled','applely']

for w in example_word:
	print(ps.stem(w))

new_input = 'An apple a day keep the appler appling.'

words = word_tokenize(new_input)

for z in words:
	print(ps.stem(z))

## Stemming is a method to identify similar words used.