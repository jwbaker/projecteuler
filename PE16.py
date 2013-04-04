'''
Created on 2013-03-27

Problem 16:
2^15 = 327628 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

SOLUTION: 1366
@author: Jason Baker
'''

# Python makes this problem very easy, because of how easily it converts between different data types
def sumDigits(num):
    total = 0;
    
    for s in str(num):
        total += int(s);
        
    return total;

print(sumDigits(2**1000));