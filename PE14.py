'''
Created on 2013-03-27

Problem 14:
The following iterative sequence is defined for the set of positive integers:
    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)
    
Using the role above and starting with 13, we generate the following sequence:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1. 

Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
@author: Jason Baker
'''

def collatzLengthHelp(start, acc):
    if start == 1: return acc + 1;
    elif start % 2 == 0:
        return collatzLengthHelp(start/2, acc + 1);
    else:
        return collatzLengthHelp((3 * start) + 1, acc + 1);

def collatzLength(start):
    return collatzLengthHelp(start, 0);

largestLength = 1;
largestNum = 1;

for i in range (1, 1000001):
    nextLength = collatzLength(i);
    if nextLength > largestLength:
        largestNum = i;
        largestLength = nextLength;
    
print(largestNum);