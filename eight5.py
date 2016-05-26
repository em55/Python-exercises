from find import *

def count(w, l):
	count = 0
	i = 0
	length = len(w)-1
	while i <= length:
		i = find(w,l,i)
		if i != -1:
			count = count + 1

	print l, ":", count

count("troublemaker", "r")