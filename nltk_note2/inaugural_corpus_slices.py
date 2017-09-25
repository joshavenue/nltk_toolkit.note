import nltk
import os
from nltk.corpus import inaugural

count = 0

print(inaugural.fileids())
os.system('clear')
print(len(inaugural.fileids()))

x = [fileid[5:-4:] for fileid in inaugural.fileids()]		## Since the first 4 char is the year
y = [fileid[:4] for fileid in inaugural.fileids()]

print(x)

print(y)