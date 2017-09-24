
def count_char(text,char):
	return text.count(char)

find_letter = str(input('Enter a letter : '))

with open('hi.txt') as f:
	text = f.read()

print(count_char(text, find_letter))
