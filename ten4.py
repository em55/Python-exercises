""" This program takes a list from the user and prints all elements in the middle of the list, excluding the first and last elements"""

input_list = raw_input("Enter a list of elements separated by a space: ").split()

def middle(n):
	return n[1:-1]

print input_list
print middle(input_list)

