'''
Created on 2013-04-03

Problem 23:
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the
proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant
numbers is 24. By mathematical analysis, it can be shown that all integers greater than 2813 can be written as the sum of two 
abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all positive integers which cannot be written as the sum of two abundant numbers.
@author: Jason Baker
'''

def sumOneToN(n):
    return int( (n * (n - 1)) / 2 );

def sumProperDivisors(num):
    divisorSum = 0;
    
    for i in range(1, num):
        if num%i == 0:
            divisorSum += i;
    return divisorSum;

def arrayContains(arr, target):
    if len(arr) == 0: return False;
    
    for i in arr:
        if i == target:
            return True;
    return False;

def isAbundant(num):
    if sumProperDivisors(num) > num:
        return True;
    else:
        return False;

def abundantNumbers(limit):
    result = [];
    num = 12;
    
    while num <= (limit - 12):
        if isAbundant(num):
            result += [num];
        num += 1;
        
    return result;

listAbundantNumbers = abundantNumbers(2813);
sumAbundantNumberSums = 0;
checkedSums = [];

for i in range(0, len(listAbundantNumbers)):
    for j in range(0, len(listAbundantNumbers)):
        sumIJ = listAbundantNumbers[i] + listAbundantNumbers[j];
        if sumIJ <= 2813 and not arrayContains(checkedSums, sumIJ):
            sumAbundantNumberSums += sumIJ;
            checkedSums += [sumIJ];
            
print(sumOneToN(2813) - sumAbundantNumberSums);