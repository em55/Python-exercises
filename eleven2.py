"""This program counts the frequency of letters in a word"""
def histogram(s):
	d = dict()
	for c in s:
		d[c] = 1 + d.get(c,0)
	return d

word = raw_input("Enter a long word: ")

print "HISTOGRAM:", histogram(word)