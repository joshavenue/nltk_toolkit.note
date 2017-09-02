import nltk
from nltk.book import *

text1.dispersion_plot(['pain','run','hope','play'])       // Plots a graph on the dispersion of the words // 

print(sorted(set(text3))                                  // Prints out all single vocabulary in a sorted order

print(len(set(text3)))                                    // Prints out the number of length of the single occuring vocabularies

x = len(set(text3)) / len(text3)                          // This calculates the lexical richness of an entire contexts
print(x)

text3.count('God')                                        // Count how many times this word appears

// YOU CAN DO IT THIS WAY //

def lexical_diversity(text):                              // Using function to calculate lexical diversity
    return len(set(text)) / len(text)

def percentage(count, total):                             
    return 100 * count / total
