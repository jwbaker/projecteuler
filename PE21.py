'''
Created on 2013-04-03

Problem 21:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284
are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000;

SOLUTION: 31626
@author: Jason Baker
'''

def arrayContains(arr, target):
    for i in arr:
        if i == target:
            return True;
    return False;

# This is slightly different than my old factorization function, but not by much
def sumProperDivisors(num):
    divisorSum = 0;
    
    for i in range(1, num):
        if num%i == 0:
            divisorSum += i;
    return divisorSum;

amicableList = [];
sumOfAmicables = 0;

# 220 is the smallest amicable number, so we start there
num = 220;
sumDivisorsOfNum = sumProperDivisors(num);

while(num <= 10000):
    # I wish I didn't have to keep track of the sums I've already tried, but I unfortunately do because addition is not unique
    if num != sumDivisorsOfNum and not arrayContains(amicableList, sumDivisorsOfNum):
        if sumDivisorsOfNum <= 10000 and num == sumProperDivisors(sumDivisorsOfNum):
            amicableList += [num];
            amicableList += [sumDivisorsOfNum];
            # Let's just do everything in one step; halves the runtime of the program
            sumOfAmicables += num + sumDivisorsOfNum;
    num += 1;
    sumDivisorsOfNum = sumProperDivisors(num);
            
print(sumOfAmicables);