import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer as pst

train_text = state_union.raw('2005-GWBush.txt')
sample_text = state_union.raw('2006-GWBush.txt')

custom_sent_tokenizer = pst(sample_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			
			ChuckGram = r"""Chuck: {<RB.?>*<VB>*<NNP>+<NN>?}"""

			chuckParser = nltk.RegexpParser(ChuckGram)

			chucked = chuckParser.parse(tagged)

			chucked.draw()

	except Exception as e:
		pass

process_content()

## Extremely important, google POS Tagging