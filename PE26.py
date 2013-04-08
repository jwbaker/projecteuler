'''
Created on 2013-04-05

Problem 26:
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d has the longest recurring cycle in its decimal fraction part.

SOLUTION: 983
@author: Jason Baker
'''

def factor(N):
    factors = []
    
    for i in range(2, N):
        while(N % i == 0):
            factors.append(i)
            N = N/i
        if N == 1: break
    return factors

def isPrime(num):
    return len(factor(num)) == 0

def primeFactorization(N):
    result = []
    
    for i in range(2, N):
        if(N % i == 0) and isPrime(i):
            k = 1
            tmp = int( N/i )
            
            while(tmp/i % 1 == 0):
                k += 1
                tmp = int( tmp/i )
            result += [[i, k]]
            
    return result

def genNines(nines):
    return (10 * nines) + 9

def gcd(a, b):
    if a < b: return gcd(b, a)
    elif b == 0: return a
    else:
        return gcd(b, a%b)
    
def lcm(a, b):
    return int( (a/gcd(a, b)) * b )

# Finally getting more use out of this LCM function
def multLcm(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return lcm(nums[0], nums[1])
    else:
        return lcm(multLcm(nums[1:]), nums[0])
    
def findPeriod(denominator):
    factors = primeFactorization(denominator)
    # These are all the terminating decimals, so they have no recurring cycles
    if denominator == 2 or denominator == 5 or (len(factors) == 1 and (factors[0][0] == 2 or factors[0][0] == 5)) or (len(factors) == 2 and factors[0][0] == 2 and factors[1][0] == 5):
        return 0
    # Let's check the primitive primes
    elif len(factors) == 0:
        i = 1
        nines = genNines(0)
        
        while(nines%denominator > 0):
            i += 1
            nines = genNines(nines)
            
        return i
    # Now for composite numbers
    else:
        # Fun property of integers not co-prime to 10: when you strip out the 2s and 5s, they're just like any others
        if denominator % 2 == 0 or denominator % 5 == 0:
            while denominator/2 % 1 == 0:
                denominator = int( denominator/2 )
            while denominator/5 % 1 == 0:
                denominator = int( denominator/5 )
            return findPeriod(denominator)
        
        # Some special cases that require special handling
        if denominator == 3:
            return 1
        elif denominator == 487:
            return 486
        # Now we can get to the real meat of the algorithm
        primePeriods = []
        
        for f in factors:
            # 3 is still a special case
            if f[0] == 3:
                if f[1] == 1:
                    primePeriods += [1]
                else:
                    primePeriods += [ f[0]**(f[1] - 2) ]
            else:
                # A funny little property that makes this algorithm nice and quick
                primePeriods += [ f[0]**(f[1] - 1) * findPeriod(f[0]) ]
        return multLcm(primePeriods)

#print(findPeriod(867))
largestCycle = 0
d = 0

for i in range(2, 1000):
    cycle = findPeriod(i)
    if cycle > largestCycle:
        largestCycle = cycle
        d = i
        
print(d)