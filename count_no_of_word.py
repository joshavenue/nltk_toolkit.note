def count_char(text,char):
	return text.count(char)

filename = input('Enter a filename : ')
find_letter = str(input('Enter a letter : '))

with open(filename) as f:
	text = f.read()

print(count_char(text, find_letter))
