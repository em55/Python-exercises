def rotate_word(s, n):
	a = ''
	for c in s:
		a += chr(ord(c)+n)
	return a 	

input_string = raw_input("Enter the word to be encrypted: ")
rot_amount = int(raw_input("Enter the number of rotations: "))

print "Rotated word is ", rotate_word(input_string, rot_amount)

