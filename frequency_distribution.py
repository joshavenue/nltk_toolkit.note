import nltk
from nltk.book import *

x = FreqDist(text3)             // Assign a variable x with a frequency distribution

print(x)

print(x.most_common(50))        // Prints top 50 most common words

y = set(text1)                                            // All set of various vocabulary
long_words = [word for word in y if len(word) > 15]       // Create a for loop...if condition that print any word more than 15 letters
print(sorted(long_words))                 

print(len(sorted(long_words))                 

