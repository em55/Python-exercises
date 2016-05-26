def has_no_e(w):
	if w.find('e', 0, len(w)) == -1:
		return True
	return False

e_count = 0
fin = open('words.txt')

for line in fin:
	word = line.strip()
	if has_no_e(word) == True:
		e_count = e_count + 1
		print word

fin.close()
e_count = float(e_count)
print "{} percent of words in the list do not have an 'e'".format(round((e_count/113809.0)*100, 3))