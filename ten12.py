def main():
	wordlist = []
	fin = open('words.txt')
	for word in fin:
		word = word.strip()
		wordlist.append(word)
	print len(wordlist)
	print "Reverse pairs are: \n"
	rev_pairs(wordlist)

def rev_pairs(wlist):
	for word in wlist:
		for cword in wlist:
			if word == cword[::-1]:
				if wlist.index(word) != wlist.index(cword):
					print word, cword



main()