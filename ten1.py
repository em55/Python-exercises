def combine(num):
	i=0
	for i in range(len(num)):
		if type(num[i]) is list:
			combine(num[i])
		else:
		
			big_list.append(num[i])
	return big_list

big_list = []
a = [1,[1,2,3,4,[5,6,7],[1,2,3],[4,5,6,10]]]

combine(a)
print big_list
print sum(big_list)

