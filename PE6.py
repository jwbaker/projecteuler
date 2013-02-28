'''
Created on 2013-02-28

Problem 6:
The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers if (1 + 2 + ... + 10)^2 + 55^2 = 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
@author: Jason Baker
'''

def sum1toN(N):
    return int( (N * (N + 1))/2 )

def sumSquares1toN(N):
    if N == 1: return 1
    else:
        return N**2 + sumSquares1toN(N-1)

N = 100

print(sum1toN(N)**2 - sumSquares1toN(N))