import nltk
from nltk.corpus import brown

print(brown.categories())

genre_word = [(genre, word)                               ## You have Genre and Word
				for genre in ['news', 'romance','hobbies']        ## For genre in the selected genre
				for word in brown.words(categories=genre)]        ## For words in the selected genre


cfd_1 = nltk.ConditionalFreqDist(genre_word)              ## Use a conditional freq distribution method for the variable

print(cfd_1.conditions())

print(cfd_1['news'])                                      ## You will see the number of samples and outcome 
print(cfd_1['romance'])
print(cfd_1['hobbies'])
