import random

def is_anagram(a,b):
	for i in range(200):
		if b == ''.join(random.sample(a,len(a))):
			return True
	return False

print is_anagram("decty", "tedey")
