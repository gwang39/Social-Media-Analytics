__author__ = 'piorkja1'

import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer

def get_tokens():
	with open('reddit.txt') as stem:
		tokens = nltk.word_tokenize(stem.read())
	return tokens

def do_stemming(filtered):
	stemmed = []
	for f in filtered:
		#stemmed.append(PorterStemmer().stem(f))
		#stemmed.append(LancasterStemmer().stem(f))
		stemmed.append(SnowballStemmer('english').stem(f))
	return stemmed

if __name__ == "__main__":

	tokens = get_tokens()

	stemmed_tokens = do_stemming(tokens)

	result = dict(zip(tokens, stemmed_tokens))
	print("{tokens:stemmed} = ",  result)