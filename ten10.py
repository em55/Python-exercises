import time

def main():
	t1 = time.time()
	one_element = []
	append(one_element)
	print "Append function - Time:", time.time()-t1
	print len(one_element)
	
	t1 = time.time()
	two_element = []
	idiom(two_element)
	print "Idiom - Time:", time.time()-t1
	print len(two_element)
	
def append(elem_list):
	fin = open('words.txt')
	for word in fin:
		word = word.strip()
		elem_list.append(word)
	fin.close()
	return elem_list

def idiom(elem_list):
	fin = open('words.txt')
	for word in fin:
		word = word.strip()
		elem_list = elem_list + [word]
	fin.close()
	return elem_list

main()

