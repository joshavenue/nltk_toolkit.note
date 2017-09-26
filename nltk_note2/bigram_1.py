import nltk

sent = ['In', 'the','beginning','God','created','the','heaven','and','the','earth']

x = list(nltk.bigrams(sent))

print(x)

## Generated outcome . : [('In', 'the'), ('the', 'beginning'), ('beginning', 'God'), ('God', 'created'), 
##                       ('created', 'the'), ('the', 'heaven'), ('heaven', 'and'), ('and', 'the'), 
                         ('the', 'earth')]
