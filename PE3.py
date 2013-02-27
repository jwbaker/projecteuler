'''
Created on 2013-02-27

Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

@author: Jason Baker
'''

import math

def isInteger(a):
    return (a%1 == 0)

def factor(N):
    a = math.ceil(math.sqrt(N))
    b = a**2 - N
    
    while(not isInteger(math.sqrt(b))):
        a += 1
        b = a**2 - N
    
    if a - math.sqrt(b) == N:
        return int(a - math.sqrt(b)), int(a + math.sqrt(b))
    else:
        return factor(int(a - math.sqrt(b))), factor(int(a + math.sqrt(b)))
        

#def multFactor(n):
#    if factor(n) == n: print(n)
#    else:
#        factors = factor(n)
#        for f in factors:
#            return multFactor(f)

print(factor(600851475143))