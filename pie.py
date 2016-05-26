from polygon import *

world = TurtleWorld()    
bob = Turtle()
bob.delay = 0.001

def triangle(t, n, l):
	
		polygon(t, 3, l)
	#	lt(t, 180-angle)
	

def pie(t, n, l):
	
	for i in range(n):
		triangle(t, n, l)
		lt(t, 360/n)

def move():	
	pu(bob)
	rt(bob, 5)
	fd(bob, 250)
	pd(bob)

print bob
pie(bob, 5, 50)
move()
pie(bob, 6, 60)
move()
pie(bob, 7, 70)


wait_for_user()
