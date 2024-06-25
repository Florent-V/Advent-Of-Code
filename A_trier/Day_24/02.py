#!/usr/bin/env python3

import sys
import re
import math
from collections import namedtuple

Hailstone = namedtuple('Hailstone', ('x', 'y', 'z', 'dx', 'dy', 'dz'))

IDENTICAL = object()
#MIN, MAX = 7, 27
MIN, MAX = 200000000000000, 400000000000000
DEBUG = True

def intersect(h1, h2):
	a1 = h1.dy/h1.dx
	b1 = h1.y - a1*h1.x
	a2 = h2.dy/h2.dx
	b2 = h2.y - a2*h2.x
	if math.isclose(a1, a2):
		if math.isclose(b1, b2):
			return IDENTICAL
		return None # parallel
	cx = (b2-b1)/(a1-a2)
	cy = cx*a1 + b1
	in_future = (cx > h1.x) == (h1.dx > 0) and (cx > h2.x) == (h2.dx > 0)
	return (in_future, cx, cy)

def main():
	hailstones = []
	for line in sys.stdin.readlines():
		hailstones.append(Hailstone(*map(int, re.split(r'\s*[,@]\s*', line))))
	count = 0
	for i, h1 in enumerate(hailstones[:-1]):
		for h2 in hailstones[i+1:]:
			if DEBUG:
				print('Hailstone A:', h1)
				print('Hailstone B:', h2)
			c = intersect(h1, h2)
			if not c:
				if DEBUG: print('Parallel')
			elif c == IDENTICAL:
				if DEBUG: print('Identical')
				count += 1
			else:
				in_future, cx, cy = c
				if in_future:
					if DEBUG: print('Interesect at x=', cx, 'y=', cy)
					if MIN <= cx <= MAX and MIN <= cy <= MAX:
					   count += 1
				else:
					if DEBUG: print('In the past')
			print()
	print(count)

if __name__ == '__main__':
	main()