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

import re 
@[A-Za-z0-9_]+ Start with an @ and then any number of digits, characters or underscore
[w for w in words if re.search('@[A-Za-z0-9_]+', w)] searches through all words and finds those, that are callouts (start with @)