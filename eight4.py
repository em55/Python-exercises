""" This program finds and prints the index of the letter in the word given. It starts looking from the index position i"""
def find(word, letter, i):
	index = i
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1

word = raw_input("Enter a word: ")
letter = raw_input("Enter a letter to search for: ")
index = int(raw_input("Enter a position to start searching (0 for the whole string): "))
print find(word, letter, index)
