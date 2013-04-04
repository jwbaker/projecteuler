'''
Created on 2013-02-28

Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

SOLUTION: 142913828922
@author:Jason Baker
'''
# This was my first method. It works, but it takes a long time to run
# That factorization function again, slightly modified this time
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

# At this point I still haven't found a better way to generate primes than just guessing and checking
for i in range (2, N):
    if isPrime(i):
        total = total + i
        
print(total)

# I tried the problem again using the Sieve of Eratosthenes algorithm, but the recursion depth was too great for an upper bound of 2 million

# Create the list of numbers to pass into the sieve
# Each number has a boolean value associated with it; this value will be true only if the number is prime, but for now it's always true
#def listToNForSieve(n):
#    result = [];
#    for i in range(2, n + 1):
#        result += [[i, True]];
#    return result;
#
#def eratosthenes(numbers, nextPrime = 2, pIndex = 0):
#    for i in range(pIndex + nextPrime, len(numbers), nextPrime):
#            numbers[i][1] = False;
#    for i in range(pIndex + 1, len(numbers)):
#        if numbers[i][1]:
#            return eratosthenes(numbers, numbers[i][0], i);
#    primes = [];
#    
#    for i in range(0, len(numbers)):
#        if numbers[i][1]:
#            primes.append(numbers[i][0]);
#    return primes;
#        
#N = 2000000;
#sumPrimes = 0;
#
#for p in eratosthenes(listToNForSieve(N)):
#    sumPrimes += p;
#    
#print(sumPrimes);