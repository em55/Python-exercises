def uses_only(w, f):
	for c in w:
		if c not in f:
			return False
	return True

def main():

	f = raw_input("Enter the list of letters to display words that use only them: ")
	fin = open('words.txt')

	for line in fin:
		word = line.strip()
		if uses_only(word, f) == True:
			print word

	fin.close()

main()