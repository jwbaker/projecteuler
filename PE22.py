'''
Created on 2013-04-03

Problem 22:
Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it
into alphabetical order. Then working out the alphabetical value for each name, multiple this value by its alphabetical position in the
list to obtain a name score.

FOr example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file? 
@author: Jason Baker
'''
import re;
import math;

def merge(ls, rs):
    result = [];
    i = 0;
    j = 0;
    
    while i < len(ls) and j < len(rs):
        if ls[i] <= rs[j]:
            result += [ ls[i] ];
            i += 1;
        else:
            result += [ rs[j] ];
            j += 1;
    result += ls[i:];
    result += rs[j:];
    return result;

def mergeSort(arr):
    if len(arr) <= 1:
        return arr;
    
    midPoint = int( math.floor(len(arr)/2) );
    
    left = mergeSort(arr[:midPoint]);
    right = mergeSort(arr[midPoint:]);
    
    return merge(left, right);

def nameScore(name):
    score = 0;
    for c in name:
        if c != "\"":
            score += ord(c) - ord('A') + 1;
    return score;

buffer = open("names.txt").read();
names = re.findall(r'"[^"]*"',buffer);

namesSort = mergeSort(names);

sumScores = 0;

for i in range(0, len(namesSort)):
    sumScores += nameScore(namesSort[i]) * (i + 1);
    
print(sumScores);