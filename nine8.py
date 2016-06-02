def rule(n):
	return (is_palindrome(n, 2, 4) and 
		is_palindrome(n+1, 0, 5) and 
		is_palindrome(n+2, 1, 4) and
		is_palindrome(n+3, 0, 6))
		
def is_palindrome(i, start, end):
	i = str(i)[start:start+end]
	return i == i[::-1]
def main():

	s = 0
	for num in range(100000,999999):
		if rule(num):
			s = s + 1
			print "The number is ", num
	print "count: ", s
	
main()