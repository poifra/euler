import utils
import math

def prob52():
    '''
    Permutted multiples
    It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
    '''
    found = False
    i = 1
    while not(found):
        if utils.is_perm(i,2*i) and utils.is_perm(i,3*i) and utils.is_perm(i,4*i) and utils.is_perm(i,5*i) and utils.is_perm(i,6*i):
            return i
        i += 1

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

def prob60():
    import itertools
    combs = itertools.combinations(utils.genPrimes(int(1e5)),5)
    for combo in combs:
        concats = itertools.combinations(combo,2)
        allPrimes = True
        for conc in concats:
            leftRight = int(str(conc[0])+str(conc[1]))
            rightLeft = int(str(conc[1])+str(conc[0]))
            if not utils.isPrime(leftRight) or not utils.isPrime(rightLeft):
                allPrimes = False
            if not allPrimes:
                break
        if allPrimes:
            return combo,sum(combo)

def prob67():
    '''
    max sum II, non bruteforce edition
    This is the same as prob 18, but with a much bigger scale.
    This time we use dynamic programming, we add up maximums, starting from the bottom of the triangle.
    '''
    highest = 0
    size = 100
    lst = [[]*size]*size
    with open('prob67text.txt','r') as f:
        data = f.read().split('\n')
        for i,line in enumerate(data):
            numbers = line.split(' ')
            lst[i] = list(map(int,numbers)) + [0]*(size-len(numbers))

    for i in range(size-2, -1, -1):
        for j in range(i+1):
            lst[i][j] += max(lst[i+1][j],lst[i+1][j+1])
    return lst[0][0]

def prob92():
    limit = int(1e7)
    count = 0
    for i in range(1,limit):
        n = i
        while n != 1 and n != 89:
            n = sum(int(k)**2 for k in list(str(n)))
        if n==1:
     #       print(i)
            count += 1
    return limit - count
