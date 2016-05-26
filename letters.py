from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.005

def draw_a():
	lt(bob, 60)
	fd(bob, 40)
	rt(bob, 120)
	fd(bob, 40)
	pu(bob)
	bk(bob, 20)
	pd(bob)
	rt(bob, 120)
	fd(bob, 20)

def draw_b():
	lt(bob, 90)
	fd(bob, 40)
	rt(bob, 120)
	fd(bob, 40)
	pu(bob)
	bk(bob, 20)
	pd(bob)
	rt(bob, 120)
	fd(bob, 20)

draw_b()

