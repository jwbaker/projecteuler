'''
Created on 2013-03-27

Problem 17:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage. 
@author: Jason Baker
'''
import math;

def sumDigit(num):
    if num == 1 or num == 2 or num == 6:
        return 3;
    elif num == 4 or num == 5 or num == 9:
        return 4;
    elif num == 3 or num == 7 or num == 8:
        return 5;
    else:
        return 0;
    
def sumTeens():
    total = len("ten") + len("eleven") + len("twelve");
    
    for i in range(3, 10):
        if i == 3: total += len("thir");
        elif i == 5: total += len("fif");
        else: total += sumDigit(i);
        
        total += len("teen");
        return total;
        
def sumTen(num):
    total = 0;
    
    if num == 2: total += len("twen");
    elif num == 3: total += len("thir");
    elif num == 5: total += len("fif");
    else: total += sumDigit(num);
    
    total += len("ty");
    return total;

# This will be a highly specialized mini-program, rather than a generic algorithm
# I may come back later and fix this
total = 0

# We're only summing to 1000, so we'll only have one instance of "thousand"
total += len("thousand");

# 999 numbers left
# The first 99 won't have the word "hundred", but the others all will
total += 900 * len("hundred");

# Of those 900, all except for the even 00's will have an "and"
# There will be 9 even 00's
total += 891 * len("and");

# There will be nine hundred-blocks
for i in range (1, 10):
    # Each hundred-block will have a top-level digit once
    total += sumDigit(i);
    
    # Each hundred block will also have a teens block
    total += sumTeens();
    
    # In addition to the teens, each hundreds block will have 8 tens blocks
    for j in range (2, 10):
        # Each tens block will have 10 occurrences of its name
        total += 10 * sumTen(j);
        
        # Each tens block will also have one occurrence of each single digit
        for k in range(1, 10):
            total += sumDigit(k);
            
# In the 0th hundreds block, there will be another set of teen block and tens blocks
total += sumTeens();
    
for j in range (2, 10):
    total += 10 * sumTen(j);
    
    for k in range(1, 10):
        total += sumDigit(k);
        
# Finally, there will be a single occurrence of each single digit
for k in range(1, 10):
    total += sumDigit(k);

#Print the result
print(total);