# text1 = "Ethics are built built right into the ideals and objectives of the United Nations"
# words = text1.split(' ')
# long_words = [w for w in words if len(w) > 3]
# unique_words = set(words)
# print([w for w in words if w.startswith('i')])


import nltk
#from nltk.book import *
# porter = nltk.PorterStemmer()
# testsentence = 'Das ist ein echt cooler Satz, der geht. Und jeder ging nach Hause.' 
# words = nltk.word_tokenize(testsentence)
# result = [porter.stem(t) for t in words]
# print(result)
# print(nltk.help.upenn_tagset('MD'))
text15 = nltk.word_tokenize('Alice loves Bob')
