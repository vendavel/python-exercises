from math import *

def compare(x, y):
	if x > y: return 1
	elif y > x: return -1
	else: return 0

def hypotenuse(a,b):
	temp = sqrt(a ** 2 + b ** 2)
	print temp
	return 0.0

print hypotenuse(1,2)