_author__ = 'piorkja1'

import nltk



stem = open('twitterjhu.txt','r')
wtokens = nltk.word_tokenize(stem.read())
stem = open('twitterjhu.txt','r')
ctokens = nltk.casual_tokenize(stem.read())
stem = open('twitterjhu.txt','r')
stokens = nltk.sent_tokenize(stem.read())



print("word tokens = ",  wtokens)
print("casual tokens = ",  ctokens)
print("sentence tokens = ",  stokens)

file = open("tokenoutput.txt", "w")
file.write("word tokens " + '\n')
for item in wtokens:
  file.write("%s\n" % item)
file.write("casual tokens " + '\n')
for item in ctokens:
  file.write("%s\n" % item)
file.write("sentence tokens " + '\n')
for item in stokens:
  file.write("%s\n" % item)
