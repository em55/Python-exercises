def is_abecedarian(w):
	return all(c >= w[:1] for c in w[1:])

def main():

	fin = open('words.txt')
	count = 0
	for line in fin:
		w = line.strip()
		if is_abecedarian(w):# w==sorted(w)
			count = count + 1
			print w

	fin.close()
	print "There are {} abecedarian words in the list.".format(count)

main()