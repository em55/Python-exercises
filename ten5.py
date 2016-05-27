a = [1,2,3,4,5,6,7,8,9,0]

def chop(n):
	n.pop(0)
	n.pop(-1)
	

print chop(a)
print a