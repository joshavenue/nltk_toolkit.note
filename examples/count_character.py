def count_char(text,char):
	return text.count(char)

filename = open('hi.txt')
with open('hi.txt') as f:
	text = f.read()

for char in 'abcdefghijklmnopqrstuvwxyz':
	perc = 100 * count_char(text,char) / len(text)
	print('{0} - {1}%'.format(char,round(perc,2)))
  
  ## To find out percentage of different letters used. ##
