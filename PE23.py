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

SOLUTION: ???
@author: Jason Baker
'''

def sumOneToN(N):
    return int( (N * (N - 1))/2 );

def arrayContains(arr, target):
    for i in arr:
        if i == target:
            return True;
    return False;

def sumProperDivisors(num):
    divisorSum = 0;
    
    for i in range(1, num):
        if num%i == 0:
            divisorSum += i;
    return divisorSum;

def isAbundant(num):
    return sumProperDivisors(num) > num

def listAbundantsTo(limit):
    result = [];
    
    for i in range(12, limit + 1):
        if isAbundant(i):
            result += [i];
    return result;

N = 28123;

abundantList = listAbundantsTo(N);
sumToN = sumOneToN(N);
checkedSums = [];

for i in abundantList:
    for j in abundantList:
        sumIJ = i + j;
        if sumIJ <= N and not arrayContains(checkedSums, sumIJ):
            sumToN -= sumIJ;
            checkedSums.append(sumIJ);

print(sumToN);