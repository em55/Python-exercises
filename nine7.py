def rule(w):
	count = 0
	i = len(w)-1
	while i > 0:
		if w[i] == w[i-1]:
			count = count+1 
			if count == 3:
				return True
			i = i - 2 
		else:
			count = 0
			i = i - 1
	return False

def main():

	fin = open('words.txt')
	s = 0
	for line in fin:
		w = line.strip()
		if rule(w) == True:
			s = s + 1
			print "The word is ", w

	fin.close()
	print "count: ", s
	
main()