s = "redivider"
def is_palindrome(s):
	if s[0:len(s)] == s[::-1]:
		return True
	return False

print is_palindrome(s)