def remove_duplicates(a):
	new_list = []
	for char in a:
		if char not in new_list:
			new_list.append(char)
	return new_list

sample = [1,4,1,5,4,3,5,6,8,9,0,1,2,3,4,5,6,7,"cat","dog","cat"]

print remove_duplicates(sample)
