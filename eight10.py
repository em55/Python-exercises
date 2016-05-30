""" This program checks if the given string is a palindrome"""

s = raw_input("Enter a string: ")
def is_palindrome(s):
	if s[0:len(s)] == s[::-1]:
		return "It is a palindrome"
	return "It is not a palindrome"

print is_palindrome(s)