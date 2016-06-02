a = 'abs'

def is_sorted(n):
	i = 0
	p = 0 
	while i < len(n):
		if n[i] < p:
			return False
		p = n[i]
		i = i + 1
	return True
	
print is_sorted(a)
