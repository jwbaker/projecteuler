'''
Created on 2013-04-05

Problem 25:
The Fibonacci sequence is defined by the recurrence relation:

F_n = F_n-1 + F_n-2, where F_1 = 1 and F_2 = 1.

Hence, the first 12 terms will be:
F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144

The 12th term, F_12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

SOLUTION: 4782
@author: Jason Baker
'''

# The closed formula I used in PE2 won't work here because the numbers are too big
# Have to do this the old-fashioned way
def fib(fib1, fib2):
    return fib1 + fib2

# Convenience method, more than anything else
def numDigits(num):
    return len(str(num))

size = 1000

lastFib = 1
nextFib = 1
index = 2

while(numDigits(nextFib) < size):
    temp = nextFib
    nextFib = fib(nextFib, lastFib)
    lastFib = temp
    index += 1
    
print(index)