"""This program prints a list of all keys that match a given value using reverse lookup method"""
def histogram(s):
	d = dict()
	for c in s:
		d[c] = 1 + d.get(c,0)
	return d

def reverse_lookup(d, v):
	l = list()
	for k in d:
		if d[k] == v:
			l.insert(len(l), k)
	return l
	#return [k for k,val in d.items() if val == v]
	

def main():
	word = raw_input("Enter a long word: ")
	d = histogram(word)
	print d
	v = int(raw_input("Enter a value to lookup in the dictionary: "))
	print reverse_lookup(d,v)

main()
