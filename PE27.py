'''
Created on 2013-04-07

Problem 27:
Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40
+ 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41,

Using computers, the incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to
79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the formL

n^2 + an + b, where |a| < 1000 and |b| < 1000
where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0

SOLUTION: ???
@author: Jason Baker
'''

def factor(N):
    factors = []
    
    for i in range(2, int(N/2)):
        while(N % i == 0):
            factors.append(i)
            N = N/i
        if N == 1: break
    return factors

def isPrime(num):
    return len(factor(num)) == 0

def lengthOfPrimeSequence(a, b):
    if b == 0:
        return 0
    n = 0
    
    while(True):
        x = n**2 + (n * a) + b
        if n > 0 and n % b == 0:
            break
        elif (n + a) % b == 0:
            break
        elif not isPrime(x):
            break
        else:
            n += 1
        
    return n + 1

longestSequence = 0
largestPair = [0, 0]
for a in range(-999, 1000):
    for b in range(-999, 1000):
        primeSequence = lengthOfPrimeSequence(a, b)
        print(str(a) + ", " + str(b) + " = " + str(primeSequence))
        if primeSequence > longestSequence:
            longestSequence = primeSequence
            largestPair[0] = a
            largestPair[1] = b
    
print(largestPair[0] * largestPair[1])

## These sets are equivalent: opportunity for efficiency
#print(lengthOfPrimeSequence(-1, 41))
#print(lengthOfPrimeSequence(-1, -41))
#
#print(lengthOfPrimeSequence(-79, 1601))
#print(lengthOfPrimeSequence(-79, -1601))