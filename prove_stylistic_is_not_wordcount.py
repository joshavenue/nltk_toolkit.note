import nltk
from nltk.corpus import brown

find_text = brown.words(categories = 'lore')

frequency_dist = nltk.FreqDist(w.lower() for w in find_text)

modals = ['may', 'will']

for m in modals:
	print(m, ' : ', frequency_dist[m], end= '\n')

z = find_text.count('will')

print('the number of times the word \'will\' appeared is : {}'.format(z))