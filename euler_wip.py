import utils
import math

def prob41():
    #pandigital primes
    limit = 7654321 #we exploit the property that if the sum of digits of a number is divisible by 3, the number is divisible by 3
    numbers = "".join([str(i) for i in range(1,len(str(limit))+1)])
    for x in range(limit,1,-2):
        if all(str(x).count(y) == 1 for y in numbers):
            if utils.isPrime(x):
                return x

def prob42():
    #the longest word in the file is of length 14, 14*20 = 364, closest triangle is t(26) = 351 
    limit = 26
    alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    triangles = [0.5*n*(n+1) for n in range(1,limit+1)]
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
        if int(x[1]+x[2]+x[3])%2==0 
            and int(x[2]+x[3]+x[4])%3==0 
            and int(x[3]+x[4]+x[5])%5==0 
            and int(x[4]+x[5]+x[6])%7==0 
            and int(x[5]+x[6]+x[7])%11==0 
            and int(x[6]+x[7]+x[8])%13==0 
            and int(x[7]+x[8]+x[9])%17==0]
    return sum(map(int,subset))

def prob44():
    from math import fabs
    pentagons = [(n*(3*n-1))/2 for n in range(1,2500)]
    minD = int(10e10)
    for j in pentagons[::-1]:
        for k in pentagons[::-1]:
            if j+k in pentagons:
                d = int(fabs(j-k))
                if d in pentagons:
                    if minD > d:
                        return d
def prob45():
    #triangular, pentagonal, hexagonal
    #using dictionaries because much faster lookup
    limit = 100000
    triang = {int(n*(n+1)/2):n for n in range(2,limit)}
    penta = {int((n*(3*n-1))/2):n for n in range(2,limit)}
    hexa = {int(n*(2*n-1)):n for n in range(2,limit)}
    for n in triang:
        if n in penta and n in hexa and n > 40755:
            return n

def prob46():
    #goldbach's other conjecture:
    '''
    It was proposed by Christian Goldbach that every odd composite number 
    can be written as the sum of a prime and twice a square.

    9 = 7 + 2×1²
    15 = 7 + 2×2²
    21 = 3 + 2×3²
    25 = 7 + 2×3²
    27 = 19 + 2×2²
    33 = 31 + 2×1²

    It turns out that the conjecture was false.
    What is the smallest odd composite that cannot be written as 
    the sum of a prime and twice a square?
    '''
    from math import sqrt
    limit=6000
    primes = utils.genPrimes(limit)
    compositeOdds = [i for i in range(9,limit,2) if not utils.isPrime(i)]
    for i in compositeOdds:
        canBeWritten = False
        for n in primes:
            if (i-n) % 2 == 0:
                #we need to check if (i-n)/2  is a perfect square. if it is, i can be written as described
                num = (i-n)/2
                if num < 0: #this means we found no suitable prime
                    break
                if not (math.sqrt(num)-int(math.sqrt(num))):
                    canBeWritten=True
                    break
        if not canBeWritten:
            return i

def prob48():
    limit = 1000
    i = 0
    for x in range(1,limit+1):
        i += x**x
    return i

def prob53():
    #combinatorics selections
    def combine(n,r):
        from math import factorial as f
        return int((f(n))/(f(r)*f(n-r)))
    limit = 100
    count = 0
    for n in range(1,limit+1):
        for r in range(n):
            if combine(n,r) > int(1e6):
                count += 1
    return count

def prob56():
    #powerful digit sums
    maxS = 0
    for a in range(100):
        for b in range(1,100):
            r = a**b
            s = utils.sumOfDigits(r)
            if s > maxS:
                maxS = s
    return maxS

def prob59():
    #we know the key is 3 lowercase characters
    from itertools import combination as comb
    possibilities = list(comb([i for i in range(97,123)],3))
    with open('prob59text.txt') as f:
        numbers = list(map(int,f.read().split(',')))
