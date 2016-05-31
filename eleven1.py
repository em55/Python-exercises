"""This program searches for words in a file looking for them as keys stores in a dictionary"""
def main():
	fin = open('words.txt')
	new_dict = dict()
	for word in fin:
		word = word.strip()
		new_dict[word] = ''
		
	print len(new_dict)

	search_string = raw_input("Enter the word to search for: ")

	print find(search_string, new_dict)

def find(w, d):	
	if w in d:
		return "Found in the dictionary"
	else:
		return "Not found in the dictionary"

main()