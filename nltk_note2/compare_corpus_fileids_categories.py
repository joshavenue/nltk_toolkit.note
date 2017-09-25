import nltk
from nltk.corpus import reuters
from nltk.corpus import brown
import os

count_1_1 = 0
count_2_1 = 0

count_1_2 = 0
count_2_2 = 0

for fileid_1 in brown.fileids():
	print(fileid_1, end='\n')
	count_1_1 += 1

for fileid_2 in reuters.fileids():
	print(fileid_2, end='\n')
	count_1_2 += 1

for file_categories_1 in brown.categories():
	print(file_categories_1, end='\n')
	count_2_1 += 1

for file_categories_2 in reuters.categories():
	print(file_categories_2, end='\n')
	count_2_2 += 1

os.system('clear')

print('File ID for Brown corpus : {}'.format(count_1_1))
print('File ID for Reuters corpus : {}'.format(count_1_2))
print('Number of categories in Brown corpus : {}'.format(count_2_1))
print('Number of categories in Reuters corpus : {}'.format(count_2_2))