"""This program finds the sum of a list of integers given as arguments"""
def sumall(*args):
	total = 0
	for n in args[0]:
		total += n
	print "sum: ", total

l = list(map(int, (raw_input("Enter a list of numbers: ").split())))

print "List of numbers: ", l
sumall(l)