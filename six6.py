def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	#print "word: ", word
	if len(word) <= 1:
		return True
	if first(word) != last(word):
		return False
	return is_palindrome(middle(word))	

name = "redivider"

print is_palindrome(name)
"""
print "first:", first(name)
print "last:", last(name)
print "middle:", middle(name)
"""
