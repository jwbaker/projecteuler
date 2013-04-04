'''
Created on 2013-02-27

Problem 4:
A palindromic number reads the same both ways. The largest palindromic number made from the product of two 2-digit numbers is 9009 = 91 x 
99.

Find the largest palindrome made from the product of two 3-digit numbers.

SOLUTION: 906609
@author: Jason Baker
'''

# I think this is a clever algorithm
# Rather than reversing the number and doing a full-length comparison, I have an iterator at each end and meet in the middle
# The algorithm is still O(n) complexity, but only takes O(n/2) time. Not a big gain, but still a gain
def isPalindrome(N):
    strN = str(N)
    length = len(strN)
    i = 0
    j = length - 1
    
    while(i < length/2):
        front = strN[i]
        back = strN[j]
        if front != back: return False
        i += 1
        j -= 1
        
    return True

largest = 1001

# All three-digit numbers
for i in range(100, 999):
    for j in range(100, 999):
        prod = i * j
        
        if isPalindrome(prod):
            if prod < largest:
                break;
            elif prod >= largest:
                largest = prod

print(largest)