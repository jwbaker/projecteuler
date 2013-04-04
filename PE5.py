'''
Created on 2013-02-28

Problem 5:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

SOLUTION: 232792560
@author: Jason Baker
'''

def gcd(a, b):
    if a < b: return gcd(b, a)
    elif b == 0: return a
    else:
        return gcd(b, a%b)
    
def lcm(a, b):
    return int( (a/gcd(a, b)) * b )

# A recursive formula that finds the lowest common multiple of a list of numbers
def multLcm(nums):
    if len(nums) == 2:
        return lcm(nums[0], nums[1])
    else:
        return lcm(multLcm(nums[1:]), nums[0])
    
def count(N):
    nums = []
    for i in range(1, N):
        nums.append(i)
    return nums

print(multLcm(count(20)))