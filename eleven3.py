"""This program prints the keys in a dictionary sorted in ascending order"""

def print_hist(h):
	for c in sorted(h):
		print c, h[c]
	
def histogram(s):
	d = dict()
	for c in s:
		d[c] = 1 + d.get(c,0)
	return d

word = raw_input("Enter a long word: ")

h = histogram(word)
print_hist(h)