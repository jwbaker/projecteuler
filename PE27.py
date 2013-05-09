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

import math

def isPrime(N):
   if N < 0: return isPrime(-1 * N)
   
   for i in range(2, int(math.sqrt(N)) + 1):
      if N % i == 0: return False
      
   return True

def lengthOfPrimeSequence(a, b):
   if b == 0:
       return 0
   n = 0
   
   while(True):
      if n == 0 or (n + a) == 0:
         if not isPrime(b): break;
      elif n == 1 and (n + a) == 1:
         if not isPrime(b + 1): break;
      elif n == 1:
         if not isPrime(b + n + a): break;
      elif (n + a) == 1:
         if not isPrime(b + n): break;
      else:
         if b % n == 0 or b % (n + a) == 0: break;
         
      n += 1
      
   return n + 1


longestSequence = 0
longestCoeffecients = [-1000, -1000]
# This is going to be a painfully ineffecient loop, but I will improve it later with symetry
for a in range(-999, 1000):
   for b in range(-999, 1000):
      currSequence = lengthOfPrimeSequence(a, b)
      if currSequence < longestSequence:
         longestSequence = currSequence
         longestCoeffecients[0] = a
         longestCoeffecients[1] = b
         
print longestCoefficients
