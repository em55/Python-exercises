import random

def has_duplicates(a):
	l = len(a)
	for i in range(l):
		for j in range(l):
			if i == j:
				continue
			elif a[i] == a[j]:
				return True
	return False

a = []
for _ in range(23):
	a.append(1000000*random.randint(1,31)+10000*random.randint(1,12)+random.randint(2000,2001))

print a
print has_duplicates(a)