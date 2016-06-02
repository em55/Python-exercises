"""This program has methods to draw these structures: square, polygon, polyline, arc, circle"""
from Tkinter import *
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def square(t, len):
	print t
	for i in range(4):
		fd(t, len)
		lt(t)

"""Draws a polygon with n sides of length l. t is a turtle"""
def polygon(t, len, n):
	polyline(t, len, n, 360)

"""Draws n line segments with length len and angle (in degrees). t is a turtle"""
def polyline(t, len, n, angle):
	print t
	for i in range(n):
		fd(t, len)
		lt(t, angle/n)

"""Draws a circle with radius r. t is a turtle"""
def circle(t, r):
	arc(t,r, 360)

"""Draws an arc of radius r and angle (in degrees). t is a turtle"""
def arc(t, r, angle):
	print t
	c = 2*3.14*r
	print c
	a = 0
	l=0
	n=0
	while a<=c:
		l = l+1
		n = n+1
		a = l*n
		print l, n, a
	
	polyline(t, l, n, angle)

arc(bob, 40, 280)

#wait_for_user()
