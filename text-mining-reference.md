# Reference for text mining

## Setup

I work from here on with these examples:  
`text1 = "Ethics are built right into the ideals and objectives of the United Nations"`
`words = ['Ethics', 'built', 'right', 'into', 'ideals', 'objectives', 'United', 'Nations']`

## Basic string information

len(text1) gives the length in characters
set(words) gives unique words
*beware of case!*
set([w.lower() for w in words]) makes each word first lowercase, than gets unique words
[w for w in words if w.startswith('#')] gets hashtags
[w for w in words if w.startswith('@')] gets callouts
list(text1) get all characters
[c in c of text1] get all characters

### string info functions

isalpha
isupper
islower
istitle
isdigit
isalnum
text1.find('the') finds the first subtext inside the text and returns its position
text1.rfind('the') finds the last subtext inside the text and returns its position

## Basic string manipulation

text1.split(' ') creates an array of words
[w for w in words if len(w) > 3] filter words with a certain length
[w for w in words if w.istitle()] filter capitalized words
[w for w in words if w.endswith('s')] filter words ending on a letter
text1.splitlines() creates an array of lines
text1.strip() removes whitespace/tabs from front and end
text1.replace('a','bc') replaces text with another

### case

text1.lower() all lowercase
text1.upper() all uppercase
text1.titlecase() first letter uppercase, other letters lowercase

## data cleaning

.strip() to clean white spaces
.replace(a,b) replaces all occurences

## File reading

f = open('blabla.txt', 'r') open in readmode
f.readline() reads next line
f.seek(0) set reading point to start of file
f.read() reads entire file
*after f.read() call splitlines() to get a line-by-line array*

## file operations

f = open(filename, mode)
f.readline()
f.read()
f.read(n) read n characters
for line in f: doSomething(line)
f.seek(n) reading position set to n
f.write(message)
f.close()
f.closed check, if file is closed

## RegExp

@[A-Za-z0-9_]+ Start with an @ and then any number of digits, characters or underscore
[w for w in words if re.search('@[A-Za-z0-9_]+', w)] searches through all words and finds those, that are callouts (start with @)

TODO: Add missing stuff

## NLP

NLTK= Natural Language Toolkit
`import nltk`
`nltk.download()` downloads text corpora
`from nltk.book import *`

texts() show all texts
sents() show all sentences
text1 acceses first text
sent1 acceses first sentence

### count vocabulary of text

len(set(text7)) unique number of words in a text
len(set(text7))[:10] first ten unique words
dist = FreqDist(text7) frequency of words
len(dist) again unique number of words in this distribution
vocab1 = dist.keys() unique words
dist[u'four'] how many times the word 'four' is used in this distribution
freqwords = [w for w in vocab1 if len(w) > 5 and dist[w] > 100] gets a list of words, which are longer then 5 characters and occur more then a hundred times

### Normalization

input1 = "List listed lists listings listings"
first: Lowercase it
words1 = input.lower().split(' ')

### Stemming

find the root of the word, the root form  
there are differend algorithmens for it  
porter = nltk.PorterStemmer()
[porter.stem(t) for t in words] gets list of words in stemmed-form

### Lemmatization

results in words that are actual meaningful
udhr = nltk.corpus.udhr.words('English-Latin1')
Stemming turns 'Universal' to 'Univers'
Lemmatization is like stemming, but results in valid words
WNlemma = nltk.WordNetLemmatizer()
[Wnlemma.lemmatize(t) for t in udhr[:20]] lemmatizes the first 20 words of the Universal Declaration of Human rights

### Tokenization

text11.split(' ') has some problems, eg 'shouldn't' would be one word, 'bed.' also one word
nltk.word_tokenize(text11) takes care of those problems

### Sentence Splitting

not all full stops end sentencens ('U.S.' or '$2.99')
sentences = nltk.sent_tokenize(text12)

### Part-of-speech (POS) tagging

verb, adverb, noun,...
nltk.help.upenn_tagset('MD') MD stands for modal auxiliary and the command shows this and all the words that are MDs

text13 = nltk.word_tokenize(text11)
nltk.pos_tag(text13) gets the POS-tags of each word

### Ambiguity in POS tagging

POS tagging gives only one version, the most likely version, not every possible version

### Parsing Sentence Structure

text15 = nltk.word_tokenize('Alice loves Bob')
S = Sentence
NP = Noun phrase (Alice, Bob)
VP = Verb phrase (loves Bob)
V = Verb (loves)

create the grammar:  
grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP
NP -> 'Alice' | 'Bob'
V -> 'loves'
""")
parser = nltk.ChartParser(grammar) parse the grammar
trees = parser.parse_all(text15)
for tree in trees:
    print tree

### Ambiguity in Parsing

"I saw the man with a telescope" - two meanings
PP = Preposition phrase (with a telescope)
parser can create all possible trees, as long as they are defined in the used grammar
treebank = large collection of possible grammar
from nltk.corpus import treebank
text17 = treebank.parsed_sents('wsj_0001.mrg')[0]
