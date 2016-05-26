def is_triangle(a,b,c):
	if (a>b+c) or (b>a+c) or (c>a+b):
		return "No"
	return "Yes"

def main():
	a = int(raw_input("Enter value a: "))
	b = int(raw_input("Enter value b: "))
	c = int(raw_input("Enter value c: "))
	print is_triangle(a,b,c)

main()
