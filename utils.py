'''
Utility library for solving project Euler problems.
Functions starting with _ are not meant to be used by other classes/modules, as per
Python's PEP suggestions.
'''
import math

'''
Constant definitions
'''
MILLER_TEST_PRECISION = 64

'''
Functions related to prime numbers
'''
def _try_composite(a, d, n, s):
    '''
    Private function used to test for primality. See isPrime.
    '''
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a,2**i * d, n) == n-1:
            return False
    return True

def isPrime(n):
    '''
    Deterministic variant of Miller-Rabin, proven correct up to 341550071728321
    Proof : http://primes.utm.edu/prove/prove2_3.html
    Adapted from code found on 
    http://rosettacode.org/wiki/Miller-Rabin_primality_test#Python
    '''

    _known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
        101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
        211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 
        337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 
        461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 
        601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 
        739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 
        881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    
    if n in (0,1):
        return False
    if n in _known_primes:
        return True

    if any((n%k) == 0 for k in _known_primes):
        return False

    #write n-1 as 2**s * d 
    d, s = n-1, 0
    while d % 2 != 0:
        d, s = d >> 1, s + 1

    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))

def genPrimes(maxBound, lowerBound=3):
    '''
    Implementation of the sieve of Eratosthenes to find all primes below n.
    '''
    l = [i for i in range(lowerBound,maxBound,2)]
    for x in range(2,int(math.sqrt(maxBound))):
        l = list(filter(lambda d: d%x != 0 or d == x, l))
    return sorted([2]+l)

def primeFactors(val):
    '''
    Returns the non-distinct prime factors of val
    '''
    for k in range(2, val): 
        if val % k == 0:
            i = int(val / k) 
            return [k] + primeFactors(i) 
    return [val]

def isTruncablePrime(n):
    leftTruncs = [n[:i] for i in range(len(n),0,-1)]
    rightTrucs = [n[i:] for i in range(len(n))]
    for l in leftTruncs:
        if not isPrime(int(l)):
            return False
    for r in rightTrucs:
        if not isPrime(int(r)):
            return False
    return True

def isCircularPrime(n):
    '''
    A circular prime is a prime number with the property that the number generated at each intermediate 
    step when cyclically permuting its (base 10) digits will be prime.
    Returns True if n is a circular prime

    This method assumes n is a string, for easier calculations on permutations.
    '''
    if len(n) == 1 and isPrime(int(n)):
        return True
    l = len(n)

    cycles = ["".join([n[i - j] for i in range(l)]) for j in range(l)]
    allPrimes = True
    for c in cycles:
        if not isPrime(int(c)):
            allPrimes = False
            break
    return allPrimes

def fact(n, proper=False):
    '''
    Finds the factors of n.
    Flag excludes last divisor (ie, returns proper divisors)
    '''
    divs = []
    for x in range(1, int(math.sqrt(n))):
        if n%x == 0:
            divs.append(x)
            divs.append(n//x)
    divs.sort()
    if proper:
        return divs[:-1]
    else:
        return divs

def collatz(n):
    '''
    Returns the Collatz sequence starting with n.
    '''
    lst = []
    lst.append(n)
    k = n
    while k != 1:
        if k % 2 == 0:
            lst.append(k//2)
        else:
            lst.append(3*k+1)
        k = lst[-1]
    return lst

'''
Functions calculating various sums.
'''
def sumOfDivisors(a):
    '''
    Returns the sum of the proper divisors of a, ie. the factors of a (excluding a itself)
    '''
    if a == 1:
        return 0

    root = int(math.sqrt(a))
    if root**2 == a: #perfect square
        s = 1+root
        root -= 1
    else:
        s = 1

    #odd numbers can only have odd numbers as divisors!
    #however, the converse is not always true
    if a % 2 == 1:
        f = 3
        step = 2
    else:
        f = 2
        step = 1

    while f <= root:
        if a%f == 0:
            s = s + f + (a // f)
        f += step
    return s

def str_sumOfDigits(s):
    '''
    Wrapper for calculating sum of digits as strings.
    '''
    return int(sumOfDigits(s))

def sumOfDigits(n):
    '''
    Returns the sum of digits in an integer n
    '''
    s = 0
    while n:
        s += n % 10 #get last digit
        n //= 10 #remove it
    return s

def sumOfFactorialDigits(n):
    #preload factorials
    f=[1,1,2,6,24,120,720,5040,40320,362880]
    s = 0
    while n:
        s += f[n%10]
        n //= 10
    return s 

def is_perm(a,b):
    '''
    Returns true if a is a permutation of b's digits
    '''
    if a==b:
        return True
    s_a = str(a)
    s_b = str(b)
    if len(s_a) != len(s_b):
        return False
    for c in s_a:
        if c not in s_b or s_a.count(c) != s_b.count(c):
            return False
    return True

    