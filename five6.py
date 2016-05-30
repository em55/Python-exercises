from swampy.TurtleWorld import *

def koch(t, x):
	if x < 3.0:
		fd(t, x)
		return
	koch(t, x/3.0)
	lt(t, 60)
	koch(t, x/3.0)
	rt(t, 120)
	koch(t, x/3.0)
	lt(t, 60)
	koch(t, x/3.0)
	
def snowflake(t,x):
	for i in range(3):
		rt(t, 120)
		koch(t,x)

def move():	
	pu(bob)
	rt(bob, 5)
	fd(bob, 250)
	pd(bob)

world = TurtleWorld()    
bob = Turtle()
bob.delay = 0.001

print bob
koch(bob, 200)
move()
snowflake(bob, 200)

wait_for_user()