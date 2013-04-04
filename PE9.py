'''
Created on 2013-02-28

Problem 9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

SOLUTION: 31875000
@author: Jason Baker
'''

def isTriple(a, b, c):
    return a**2 + b**2 == c**2
    

a = 1
b = 0
c = 0

# I had to do some back of the envelope math to get the formulas for this
# Because we're given two equations with three unknowns, it's pretty basic math to isolate for a single variable
# Then it's just a matter of incrementing that variable, and adjusting the others accordingly
while(a + b + c != 1000 and not isTriple(a, b, c)):
    a += 1
    b = int( (1000 * (a - 500))/(a - 1000) )
    c = int( (-1 * a**2 + 1000*a - 500000)/(a - 1000) )
    
print(a*b*c)