def is_abecedarian(w):
	p = 'a'
	for c in w:
		if c < p:
			return False
		p = c
	return True

def main():

	fin = open('words.txt')
	count = 0
	for line in fin:
		w = line.strip()
		if is_abecedarian(w) == True:
			count = count + 1
			print w

	fin.close()
	print "There are {} abecedarian words in the list.".format(count)

main()