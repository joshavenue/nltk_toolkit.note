import nltk
from nltk.book import *

print(text1.concordance('adventure'))     // Search the word 'adventure' from the first book using .concordance('x')

print(text1.similar('adventure'))         // Find words that are always similar in terms of context

print(text1.common_context(['pain']))  // Find the common contexts of the words

