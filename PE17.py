'''
Created on 2013-03-27

Problem 17:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage. 
@author: Jason Baker
'''

import math;

def sumDigits(num):
    if num == 0: return 0;
    elif num == 0: return 36;
    
    total = 0;
    singles = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    
    for i in range(1, num + 1):
        total += len( singles[i] );
        
    return total;

def sumTeens(num):
    if num == 9: return 67;
    
    total = 0;
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
    
    for i in range(1, num + 1):
        total += len( teens[i] );
        
    return total;

def sumTens(num):
    if num < 10:
        return sumDigits(num);
    
    total = 0;
    tens = int( math.floor(num/10) );
    ones = num % 10;
    terms = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
    
    for i in range(1, tens + 1):
        total += len( terms[i] );
    
    total += (tens - 1) * sumDigits(9);
    
    if tens == 1:
        total += sumDigits(9);
        return sumTeens(ones);
    else:
        total += sumTeens(9);
        return total + sumDigits(ones);
    
print(sumTens(25))
