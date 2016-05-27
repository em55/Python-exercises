def uses_all(w, f):
	for c in f:
		if c not in w:
			return False
	return True

def main():

	f = raw_input("Enter the list of letters to display words \n that use all of them: ")
	fin = open('words.txt')

	for line in fin:
		w = line.strip()
		if uses_all(w, f) == True:
			print w

	fin.close()

main()