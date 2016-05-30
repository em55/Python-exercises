"""This program takes a word and encrypts it usgin the ROTn method rotating the letters of the word n times""" 
#must be modified to rotate only alphabets, now it rotates among all ascii characters
def rotate_word(s, n):
	a = ''
	for c in s:
		a += chr(ord(c)+n)
	return a 	

input_string = raw_input("Enter the word to be encrypted: ")
n = int(raw_input("Enter the number of rotations: "))

print "Rotated word is ", rotate_word(input_string, n)

