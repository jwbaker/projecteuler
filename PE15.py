'''
Created on 2013-03-27

Problem 15:
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom
right corner.

How many such routes are there through a 20x20 grid?

SOLUTION: 137846528820
@author: Jason Baker
'''
import math;

# I was kicking myself for days over how long it took me to figure this one out
# This is a basic problem of combinations, and I actually solved it in my statistics class in September 2012
# The solution is C(40, 20) because every path will require 40 decisions (twice as many as the size of the square), and require moving 20 positions (the size of the square)
def latticePaths(size):
    return int( math.factorial(2*size)/(math.factorial(size)**2) );

print(latticePaths(20));