'''
Created on 2013-04-05

Problem 26:
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d has the longest recurring cycle in its decimal fraction part.

SOLUTION: ???
@author: Jason Baker
'''
import math

def factor(N):
    factors = []
    
    for i in range(2, N):
        while(N % i == 0):
            factors.append(i)
            N = N/i
        if N == 1: break
    return factors

def largestValue(arr):
    largest = 0
    
    for i in arr:
        if i > largest:
            largest = i
            
    return largest

# Simple function to generate an integer of repeating nines
def genNinesInt(nines = "", N = 1):
    for i in range(0, N):
        nines += "9"
    return int(nines)

# This method takes advantage of some fun mathematical trick
#
# In any repeating decimal where the denominator is a prime greater than 5, the recurring cycle is the numerator of a fraction where the denominator is a series of nines of the same length
# i.e. 1/7 = 0.(142857) = 142857/999999
# 
# When the denominator is not prime, we can split it into prime factors, the length of the recurring cycle is equal to the longest recurring cycle of its prime factors

# When the denominator is evenly divisible by 10, or when it is 2 or 5, it has no repeating cycles and we can ignore it
def findLengthOfUnitFractionRepetand(denominator):
    if denominator == 2 or denominator == 5 or denominator%10 == 0:
        return 0
    
    factors = factor(denominator)
    
    if len(factors) == 0:
        nines = 9
        testVal = nines/denominator
        
        while(testVal % 1 != 0):
            nines = genNinesInt(str( nines ))
            testVal = nines/denominator
        return len(str(nines))
    else:
        repetands = []
        for f in factors:
            repetands.append(findLengthOfUnitFractionRepetand(f))
        return largestValue(repetands)
    
N = 1000

largestCycleIndex = 0
largestCycleLength = 0

print(findLengthOfUnitFractionRepetand(998))

for i in range(2, N):
    lengthOfCycle = findLengthOfUnitFractionRepetand(i);
    print(lengthOfCycle)
    if lengthOfCycle > largestCycleLength:
        largestCycleIndex = i
        
print(largestCycleIndex)