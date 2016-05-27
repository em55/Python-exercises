def check(a_list, b_list):

	for a in range(100):
		for b in range(100):
			if is_palindrome(a, b):
				if a - b == 18 and a not in a_list and b not in b_list:
					a_list.append(a)
					b_list.append(b)
					return a, b


def is_palindrome(i, j):
	i,j = str(i), str(j)
	return i == j[::-1]

def main():
	a_list = []
	b_list = []
	for _ in range(8):
		a, b = check(a_list, b_list)

		print "The numbers are {}, {}".format(a,b)
	
main()