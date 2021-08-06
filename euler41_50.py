#encoding:utf-8
import math
import utils

def prob41():
    #pandigital primes
    limit = 7654321 #we exploit the property that if the sum of digits of a number is divisible by
                    #3, the number is divisible by 3
    numbers = "".join([str(i) for i in range(1,len(str(limit)) + 1)])
    for x in range(limit,1,-2):
        if all(str(x).count(y) == 1 for y in numbers):
            if utils.isPrime(x):
                return x

def prob42():
    #the longest word in the file is of length 14, 14*20 = 364, closest
    #triangle is t(26) = 351
    limit = 26
    alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    triangles = [0.5 * n * (n + 1) for n in range(1,limit + 1)]
    s = 0
    with open('prob42text.txt') as f:
        lines = f.read().split('\n')
        for word in lines:
            score = 0
            for letter in word:
                score += alphabet.index(letter)
            if score in triangles:
                s+=1
    return s

def prob43():
    #pandigital number with some property
    #dat 1 liner tho, splitted for readability
    from itertools import permutations as perm
    subset = [x for x in ["".join(y) for y in perm('0123456789') if y[0] != '0'] 
        if int(x[1] + x[2] + x[3]) % 2 == 0 and int(x[2] + x[3] + x[4]) % 3 == 0 and int(x[3] + x[4] + x[5]) % 5 == 0 and int(x[4] + x[5] + x[6]) % 7 == 0 and int(x[5] + x[6] + x[7]) % 11 == 0 and int(x[6] + x[7] + x[8]) % 13 == 0 and int(x[7] + x[8] + x[9]) % 17 == 0]
    return sum(map(int,subset))

def prob44():
    from math import fabs
    pentagons = [(n * (3 * n - 1)) / 2 for n in range(1,2500)]
    minD = int(10e10)
    for j in pentagons[::-1]:
        for k in pentagons[::-1]:
            if j + k in pentagons:
                d = int(fabs(j - k))
                if d in pentagons:
                    if minD > d:
                        return d
def prob45():
    #triangular, pentagonal, hexagonal
    #using dictionaries because much faster lookup
    limit = 100000
    triang = {int(n * (n + 1) / 2):n for n in range(2,limit)}
    penta = {int((n * (3 * n - 1)) / 2):n for n in range(2,limit)}
    hexa = {int(n * (2 * n - 1)):n for n in range(2,limit)}
    for n in triang:
        if n in penta and n in hexa and n > 40755:
            return n

def prob46():
    #goldbach's other conjecture:
    from math import sqrt
    limit = 6000
    primes = utils.genPrimes(limit)
    compositeOdds = [i for i in range(9,limit,2) if not utils.isPrime(i)]
    for i in compositeOdds:
        canBeWritten = False
        for n in primes:
            if (i - n) % 2 == 0:
                #we need to check if (i-n)/2 is a perfect square.  if it is, i
                #can be written as described
                num = (i - n) / 2
                if num < 0: #this means we found no suitable prime
                    break
                if not (math.sqrt(num) - int(math.sqrt(num))):
                    canBeWritten = True
                    break
        if not canBeWritten:
            return i

def prob47():
    '''

    The first two consecutive numbers to have two distinct prime factors are:
    14 = 2 × 7
    15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors are:
    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct prime factors. 
    What is the first of these numbers?
    '''
    pass

def prob48():
    limit = 1000
    i = 0
    for x in range(1,limit + 1):
        i += x ** x
    return i

def prob49():
    '''
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
        (i) each of the three terms are prime
        (ii) each of the 4-digit numbers are permutations of one another.
    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
    What 12-digit number do you form by concatenating the three terms in this sequence?
    '''
    primes = utils.genPrimes(10000,1001)
    for p in primes:
        if p + 3330 in primes and p + 6660 in primes:
            if utils.is_perm(p,p + 3330) and utils.is_perm(p,p + 6660) and p > 1487:
                return str(p) + str(p + 3330) + str(p + 6660)
    return None

def prob50():
    '''
    The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13
    This is the longest sum of consecutive primes that adds to a prime below one-hundred.
    The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
    Which prime, below one-million, can be written as the sum of the most consecutive primes?
    '''
    primes = utils.genPrimes(1000000)
    reversed = primes[::-1]
    
    maxLen = 0
    maxSequence = []
    for start_index in range(10):
        for i in reversed:
            total = 0
            j = start_index
            while total < i:
                total += primes[j]
                j += 1
                if(total == i):
                    sequence = primes[start_index:j]
                    if(len(sequence) > len(maxSequence)):                       
                       maxSequence = sequence
                    #   print(sequence,i)

  #  cumulSum = [sum(primes[0:i]) for i,p in enumerate(primes)][1::]
    return maxSequence,sum(maxSequence)



