def avoids(w, f):
	for c in w:
		if c in f:
			return True
	return False

def main():

	forbidden = raw_input("Enter the list of letters to avoid: ")
	fin = open('words.txt')

	for line in fin:
		word = line.strip()
		if avoids(word, forbidden) == True:
			print word

	fin.close()

main()