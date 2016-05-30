"""This program prints the names of the ducklings correctly"""
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
	if letter == 'O' or letter == 'Q':
		print letter + 'u' + suffix
		continue
	print letter + suffix

	
