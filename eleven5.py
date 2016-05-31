"""This program inverts a dictionary constructed as a histogram from a user given word""" 
def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		inverse.setdefault(val, []).append(key)
	return inverse

def histogram(s):
	d = dict()
	for c in s:
		d[c] = 1 + d.get(c,0)
	return d

def main():
	word = raw_input("Enter a long word: ")
	d = histogram(word)
	print invert_dict(d)

main()