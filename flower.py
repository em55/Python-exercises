from polygon import *

world = TurtleWorld()    
bob = Turtle()
bob.delay = 0.001

def petal(t, radius, angle):
	for i in range(2):
		arc(t, radius, angle)
		lt(t, 180-angle)
	

def flower(t, n, radius, angle):
	
	for i in range(n):
		petal(bob, radius, angle)
		lt(t, 360/n)

def move():	
	pu(bob)
	rt(bob, 5)
	fd(bob, 250)
	pd(bob)

print bob
flower(bob, 7, 60, 60)
move()
flower(bob, 10, 50, 80)
move()
flower(bob, 20, 170, 30)


wait_for_user()
