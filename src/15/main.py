"""
https://projecteuler.net/problem=15

Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?
"""

from math import factorial

# This problem is just basic combinatorics

LATTICE_LENGTH = 20
print(factorial(LATTICE_LENGTH * 2) / factorial(LATTICE_LENGTH)**2)
