'''
Created on 2013-02-28

Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

@author:Jason Baker
'''

def isPrime(N):
    factors = []
    
    for i in range(2, N):
        while(N % i == 0):
            factors.append(i)
            N = N/i
        if N == 1: break
    return len(factors) == 0

N = 2000000
total = 0

for i in range (2, N):
    if isPrime(i):
        total = total + i
        
print(total)