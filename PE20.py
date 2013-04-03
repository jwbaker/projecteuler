'''
Created on 2013-04-03

Problem 20:
n! means n x (n-1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
@author: Jason Baker
'''
import math;

def sumOfDigits(num):
    strNum = str(num);
    digitSum = 0;
    
    for c in strNum:
        digitSum += int(c);
    
    return digitSum;

print(sumOfDigits(math.factorial(100)));