'''
Created on 2013-04-03

Problem 23:
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the
proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant
numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two 
abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all positive integers which cannot be written as the sum of two abundant numbers.

SOLUTION: 4179871
@author: Jason Baker
'''

def countToN(N):
    result = [None] * N;
    
    for i in range(0, N):
        result[i] = [i + 1, True];
        
    return result;

def sumProperDivisors(num):
    divisorSum = 0;
    
    for i in range(1, num):
        if num%i == 0:
            divisorSum += i;
    return divisorSum;

def isAbundant(num):
    return sumProperDivisors(num) > num;

def listAbundantsTo(limit):
    result = [];
    for i in range(1, limit + 1):
        if isAbundant(i):
            result.append(i);
            
    return result;

N = 28123;

abundants = listAbundantsTo(N);
nums = countToN(N);

for i in range(0, len(abundants)):
    for j in abundants[i:]:
        if abundants[i] + j > N:
            break;
        nums[abundants[i] + j - 1][1] = False;
        
sumNonAbundantSums = 0;

for i in nums:
    if i[1]:
        sumNonAbundantSums += i[0];
    
print(sumNonAbundantSums)