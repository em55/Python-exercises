""" This program reads the file 'words.txt' and prints words whose length is greater than 20"""
fin = open('words.txt')

for line in fin:
	word = line.strip()
	if len(word) > 20:
		print word
fin.close()