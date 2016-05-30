import math

def hypo(a,b):
	c = math.sqrt(a**2+b**2)
	return c

side_a = int(raw_input("Enter the length of side a of the triangle: "))
side_b = int(raw_input("Enter the length of side b of the triangle: "))

print "The hypotenuse of the right triangle is of length:", hypo(side_a, side_b)