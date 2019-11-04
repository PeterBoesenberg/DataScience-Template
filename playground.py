text1 = "Ethics are built built right into the ideals and objectives of the United Nations"
words = text1.split(' ')
long_words = [w for w in words if len(w) > 3]
unique_words = set(words)
print([w for w in words if w.startswith('i')])


