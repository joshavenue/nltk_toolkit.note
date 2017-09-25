import nltk
from nltk.corpus import brown

news_text = brown.words(categories = 'news')

fdist = nltk.FreqDist(w.lower() for w in news_text)		## Find the frequency of the word appeared

modals = ['can','will','may','might','must','could']	## The modals that are used for the word search

for m in modals:
	print(m, ' : ', fdist[m], end= '\n')	


## For stylistics, not word count			