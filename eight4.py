def find(word, letter, i):
	index = i
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1


#print find('castellate', 'l', 7)
