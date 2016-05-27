a = [1,2,3,4,5,6,7,8,9,0]

def cum_sum(n):
	s = 0
	l = []
	for i in range(len(n)):
		s = s + n[i]
		n[i] = s
		l.append(n[i])
	return l

print cum_sum(a)