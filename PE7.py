'''
Created on 2013-02-28

Problem 7:
By listing the first six prime numbers: 2, 3, 5, 7, 9, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime?

SOLUTION: 104743
@author: Jason Baker
'''

# This prime factorization function is handy
def factor(N):
    factors = []
    
    for i in range(2, N):
        while(N % i == 0):
            factors.append(i)
            N = N/i
        if N == 1: break
    return factors

# Unfortunately there's no reliable formula for primes beyond the 80th or so, so we've got to do this manually
# This program takes a LONG time to run
# It doesn't lend itself in this case, but at some point in a future problem I'll have to do this using a sieving algorithm
def getPrime(n):
    primeCount = 0
    num = 1
    
    while(primeCount < n):
        num += 1
        if len(factor(num)) == 0: 
            primeCount += 1
        
    return num

print(getPrime(10001))