import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

EXAMPLE_SENT = str(input('Enter : '))

STOP_WORDS = set(stopwords.words('english'))

WORD_TOKENS = word_tokenize(EXAMPLE_SENT)

FILTERED_SENTENCE = []

for Word in WORD_TOKENS:
	if Word in STOP_WORDS:
		FILTERED_SENTENCE.append(Word)

print(WORD_TOKENS)
print(FILTERED_SENTENCE)
