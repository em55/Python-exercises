def rotate_word(s, n):
	a = ''
	for c in s:
		a += chr(ord(c)+n)
		
	print "Rotated word is ", a

rotate_word("cheer", 7)

