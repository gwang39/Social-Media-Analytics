__author__ = 'gwang39'

import json
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()

def get_tokens(file):
	return nltk.word_tokenize(file.read())

def export_tokens(tokens):
  file = open("tokenoutput.txt", "w", encoding="utf8")
  file.write("word tokens " + '\n')
  for item in tokens:
    file.write("%s\n" % item)

def do_stemming(tokens):
	stemmed = []
	for f in tokens:
		stemmed.append(PorterStemmer().stem(f))
	return stemmed

def export_stemming(tokens,stemmed_tokens):
  result = dict(zip(tokens, stemmed_tokens))
  with open('stemoutput.txt', 'w', encoding="utf8") as file:
    file.write(json.dumps(result))

def do_lemma(filtered):
	lemmize = []
	for f in filtered:
		lemmize.append(lmtzr.lemmatize(f, 'v'))
	return lemmize

def export_lemma(tokens,lemma_tokens):
  result = dict(zip(tokens, lemma_tokens))
  with open('lemmaoutput.txt', 'w', encoding="utf8") as file:
    file.write(json.dumps(result))

def main():
  filepath = 'mod2redditdata.txt'
  file = open(filepath, 'r', encoding="utf8")
  #Tokenize
  tokens = get_tokens(file)
  export_tokens(tokens)
  #Stemming
  stemmed_tokens = do_stemming(tokens)
  export_stemming(tokens, stemmed_tokens)
  #Lemmatization
  lemma_tokens = do_lemma(tokens)
  export_lemma(tokens, lemma_tokens)

def main2():
    tokens=nltk.word_tokenize("Find a good group of friends/study partners in your major. It makes studying and doing homework nicer")
    print(nltk.word_tokenize("Find a good group of friends/study partners in your major. It makes studying and doing homework nicer"))

    bgram=nltk.bigrams(tokens)

    print(do_stemming(tokens))

if __name__ == "__main__":
  main2()