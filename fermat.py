import math


def check_fermat(a,b,c,n):
	if n>2:
		if (math.pow(a,n)+math.pow(b,n)) == math.pow(c,n):
			return "Holy smokes, Fermat was wrong!"
		return "No, that doesn't work"

def main():
	a = int(raw_input("Enter value a: "))
	b = int(raw_input("Enter value b: "))
	c = int(raw_input("Enter value c: "))
	n = int(raw_input("Enter value n: "))
	print check_fermat(a,b,c,n)

main()