def remove_duplicates(in_list):
	out_list = []
	for char in in_list:
		if char not in out_list:
			out_list.append(char)
	return out_list

input_list = raw_input("Enter a list of elements separated by a space: ").split()

print remove_duplicates(input_list)
