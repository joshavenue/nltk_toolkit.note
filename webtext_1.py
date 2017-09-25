import nltk
from nltk.corpus import webtext

for fileid in webtext.fileids():
	print(fileid, ' Start : ',webtext.raw(fileid)[:50])

## This is for accessing webtext library within nltk.corpus