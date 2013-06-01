'''
Created on 2013-06-01

Problem 28:
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

*21* 22 23 25 *25*
20 *7* 8 *9* 10
19 6 *1*  2 11
18 *5* 4 *3* 12
*17* 16 15 14 *13*

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals of a 1001 by 1001 spiral formed in the same way?

SOLUTION: 669171001
@author: Jason Baker
'''

# Start with 1, since that's always going to be the center
total = 1

# To improve my algorithm over brute force, I noticed that the increment between each corner is equal to the dimension of the next corner's square minus one
# For example, 5 is in the corner of a 3x3 grid, and the difference between 5 and the previous corner(3) = 3-1 = 2
# Similarly, 13 is the corner of a 5x5 grid. The difference between 13 and the previous corner, 9, is 13 - 9 = 5 - 1 = 4
# Finally, I note that the dimension of the grid increases by 2 with each level, not by one
next = 1
for i in range(3, 1002, 2):
   for j in range(0,4):
      next += i - 1
      total += next
   
print total
