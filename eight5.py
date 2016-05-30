""" This program counts the occurences of a specified letter in a given word"""

def find(word, letter, i):
	index = i
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1

def count(w, l):
	count = 0
	i = 0
	length = len(w)-1
	while i <= length:
		i = find(w,l,i)
		if i != -1:
			count = count + 1

	print l, ":", count

word = raw_input("Enter a word: ")
letter = raw_input("Enter a letter whose frequency is to be counted: ")
count(word, letter)