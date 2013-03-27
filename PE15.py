'''
Created on 2013-03-27

Problem 15:
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routs to the bottom right corner.

How many such routes are there through a 20x20 grid?
@author: Jason Baker
'''
import math;

def latticePaths(size):
    return int( math.factorial(2*size)/(math.factorial(size)**2) );

print(latticePaths(20));