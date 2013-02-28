'''
Created on 2013-02-28

Problem 9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

@author: Jason Baker
'''

def triple(a, b, c):
    return a**2 + b**2 == c**2
    

a = 1
b = 0
c = 0

while(a + b + c != 1000 and not triple(a, b, c)):
    a += 1
    b = int( (1000 * (a - 500))/(a - 1000) )
    c = int( (-1 * a**2 + 1000*a - 500000)/(a - 1000) )
    
print(a*b*c)