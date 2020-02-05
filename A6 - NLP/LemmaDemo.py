__author__ = 'piorkja1'

import nltk

from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()


def get_tokens():
	with open('reddit.txt') as stem:
		tokens = nltk.word_tokenize(stem.read())
	return tokens

def do_lemma(filtered):
	lemmize = []
	for f in filtered:
		lemmize.append(lmtzr.lemmatize(f, 'v'))
	return lemmize

if __name__ == "__main__":

	tokens = get_tokens()
	#print("tokens = ",  tokens)

	lemma_tokens = do_lemma(tokens)
	#print("stemmed_tokens = ",  stemmed_tokens)

	result = dict(zip(tokens, lemma_tokens))
	print("{tokens:lemmas} = ",  result)
