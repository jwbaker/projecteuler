'''
Created on 2013-02-27

Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

SOLUTION: 6857
@author: Jason Baker
'''

# Simple algorithm for prime factorization
# Once we've found a prime factor, remove it from the number
# That way, we can't end up with any factors that are multiples of that prime
def factor(N):
    factors = []
    
    for i in range(2, N):
        while(N % i == 0):
            factors.append(i)
            N = N/i
        if N == 1: break
    return factors
        
factors = factor(600851475143)

largest = 1

for f in factors:
    if f > largest: largest = f
    
print(largest)