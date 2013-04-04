'''
Created on 2013-03-27

Problem 17:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and
fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

SOLUTION: 21124
@author: Jason Baker
'''
import math;

def toDigit(num):
    result = "";
    nums = ["",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
            "twenty"];
    tens = ["",
            "ten",
            "twenty",
            "thirty",
            "forty",
            "fifty",
            "sixty",
            "seventy",
            "eighty",
            "ninety"];
            
    if num <= 20:
        result += nums[num];
    else:
        result += tens[int(math.floor(num/10))];
        if num % 10 != 0:
            result += nums[num%10];
            
    return result;

# This algorithm is based off one from one of my first-year programming classes
# It only works for numbers less than 100000
def toStringHelp(arr, num, decimalPosition):
    posns = ["", "", "", "hundred", "thousand"];
    
    if decimalPosition == 0: # if we've reached the end of the number. I don't think this base case is ever actually used, but it's here just in case
        return "";
    elif decimalPosition == 1: # if the number is a single digit, there's a method for that
        return toDigit(num);
    elif decimalPosition == 2 and arr[0] == 1: # likewise if the number is a teen
        return toDigit(num);
    elif decimalPosition == 2: # or if the number is less than 100 in general
        return toDigit(num); 
    # If the number is a big round number, such 200 or 300
    elif num - (int(arr[0]) * 10**(decimalPosition - 1)) == 0 or num - (int(arr[0]) * 10**(decimalPosition - 1)) % 10**(decimalPosition - 2) == 0:
        return toDigit(int(arr[0])) + posns[decimalPosition];
    else:
        return toDigit(int(arr[0])) + posns[decimalPosition] + "and" + toStringHelp(arr[1:], num - (int(arr[0]) * 10**(decimalPosition - 1)), decimalPosition - 1);

def toString(num):
    digits = str(num);
    return toStringHelp(digits, num, len(digits));
    
def lettersOfNum(num):
    if num >= 10000:
        return "Too big";
    else:
        return toString(num);

total = 0;

for i in range(1,1001):
    total += len(lettersOfNum(i));
    
print(total);