"""This program prints words that do not contain any of the letters given by the user"""
def avoids(w, f):
	for c in w:
		if c in f:
			return False
	return True

if __name__=="__main__":

	forbidden = raw_input("Enter the list of letters to avoid: ")
	fin = open('words.txt')

	for line in fin:
		word = line.strip()
		if avoids(word, forbidden):
			print word

	fin.close()

