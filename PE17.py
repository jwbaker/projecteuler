'''
Created on 2013-03-27

Problem 17:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage. 
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

def toStringHelp(arr, num, decimalPosition):
    posns = ["", "", "", "hundred", "thousand"];
    
    if decimalPosition == 0:
        return "";
    elif decimalPosition == 1:
        return toDigit(num);
    elif decimalPosition == 2 and arr[0] == 1:
        return toDigit(num);
    elif decimalPosition == 2:
        return toDigit(num); 
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