"""This program finds the sum of a list of integers given as arguments"""
def sumall(*args):
        return sum(args[0])
	
l = list(map(int, raw_input("Enter list: ").split()))

print "List of numbers: ", l
print "sum: ", sumall(l)
