'''
Created on 2013-02-27

@author: Jason Baker
'''
import math

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