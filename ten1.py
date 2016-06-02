def combine(num):
	for i in num:
		if type(i) is list:
			combine(i)
		else:
			big_list.append(i)

big_list = []
input_list = [1,[1,2,3,4,[5,6,7],[1,2,3],[4,5,6,10]]]

combine(input_list)
print big_list
print "Sum of elements:", sum(big_list)

