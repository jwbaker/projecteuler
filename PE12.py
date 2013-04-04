'''
Created on 2013-03-05

Problem 12:
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

1: 1
3: 1, 3
6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?

SOLUTION: 76576500
@author: Jason Baker
'''
import math

def numDivisors(n):
    div = 2
    
    for i in range (2, int(math.floor(n/2)) + 1):
        if n%i == 0: div += 1
        
    return div

triag = 1
n = 3
k = 1

# Now I'm getting cleverer than just iterating over every positive integer
# To generate the triangular numbers, I'm taking advantage of a property of Pascal's Triangle, where the ith triangular number is the kth number of the (n+3)th row
# I realized later that I could also have used the closed form for the series of natural numbers, but the problem with this solution isn't generating the triangular number
while(numDivisors(triag) < 500):
    triag = math.factorial(n)/( math.factorial(k) * math.factorial(n - k) )
    n += 1
    k += 1
    
print(triag)