import utils
import math

def prob21():
    #amicable numbers
    numbers = []
    limit = 10000

    for a in range(2,limit):
        b = utils.sumOfDivisors(a)
        if b<a and utils.sumOfDivisors(b) == a:
            print(a,b)
            numbers.append(a)
            numbers.append(b)

    print(numbers)
    return sum(numbers)


def prob23():
    # non-abundant sums
    # according to magic, erm, mathematical analysis, all numbers > 28123 
    # can be written as a sum of two abundant numbers.
    # we are looking for the sum of all numbers that cannot be written as such a sum.
    limit = 28123
    is_a_sum = [False]*(limit+1)
    abundant = []
    for i in range(12,limit+1):
        if utils.sumOfDivisors(i) > i:
            abundant.append(i)

    for i in range(len(abundant)):
        #we only need to check i < j
        for j in range(i,len(abundant)):
            s = abundant[i] + abundant[j]
            if s <= limit:
                is_a_sum[s] = True
            else:
                break

    s = 0
    for i,x in enumerate(is_a_sum):
        if not x:
            s += i
    return s

def prob24():
    from itertools import permutations
    return list(permutations(range(10)))[999999]

def prob25():
    #1000 digit fibonacci number
    limit = 1000
    a = b = i = 1
    while len(str(a)) < limit:
        a,b=b,a+b
        i+=1
    return i

def prob26():
    #reciprocal cycles
    limit = 1000
    for d in range(1,limit+1):
        seen = []
        seen.append(d)
        quotient = 1//d
        while quotient == 0:
            quotient *= 10
            quotient //= d
    pass

def prob28():
    #number spiral diagobals
    #build gruid
    size = 5
    grid = [[0]*size]*size
    direction = 'r'
    n = 1
    coords = (size//2, size//2)
    while n <= size**2:
        i,j = coords
        print(i,j)
        grid[i][j] = n
        n += 1
        if direction == 'r':
            coords = (i+1,j)
            direction = 'd'
        elif direction == 'd':
            coords = (i,j+1)
            direction = 'l'
        elif direction == 'l':
            coords = (i-1,j)
            direction = 'u'
        else:
            coords = (i,j-1)
            direction = 'r'
    for i in range(len(grid)):
        for j in range(len(grid)):
            print (grid[i][j],end=' ')
        print('\n',end='')

def prob35():
    limit = 1000000
    from collections import deque
    s = 0
    candidates = [str(x) for x in range(limit) if all(char in '1379' for char in str(x))]
    circulars = set()
    for cand in candidates:
        if utils.isCircularPrime(cand):
            circulars.add(cand)
    return len(circulars) + 2 #+2 for 2 and 5, which were not included when building candidates

def prob36():
    def isPal(n):
        s = str(n)
        return s[::-1] == s
    limit = int(10e5)
    s = []
    for x in range(limit):
        if isPal(x) and isPal(bin(x)[2:]):
            s.append(x)
    return sum(s)

def prob48():
    limit = 1000
    i = 0
    for x in range(1,limit+1):
        i += x**x
    return i