'''
Created on 2013-04-05

Problem 24:
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of
the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2
are:

012 021 102 120 201 210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

SOLUTION: 2783915460
@author: Jason Baker
'''

# This method may exist in Python, but it's simple enough to do
# Returns a list containing all the elements of arr except for target
def listDiff(arr, target):
    result = [];
    
    for i in range(0, len(arr)):
        if arr[i] != target:
            result.append(arr[i])
    return result;

def permuteHelp(restSeq, acc):
    if len(restSeq) == 0:
        return acc
    else:
        concat = []
        for i in permute(restSeq):
            concat += [acc + str(i)]
        return concat

def permute(sequence):
    result = []
    
    for s in sequence:
        result += permuteHelp(listDiff(sequence, s), str(s))
    
    return result

sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
N = 1000000
print(permute(sequence)[N - 1])