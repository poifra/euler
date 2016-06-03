def prob31():
    # In England the currency is made up of pound, £, and pence, p, 
    #and there are eight coins in general circulation:
    # 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    #how many ways can we make 2 pounds

    #adapted from #31's overview
    #original was pure brute force, but took ~180 seconds to solve
    target = 200
    ways = [1] + [0]*target
    coins = [1,2,5,10,20,50,100,200]
    for coin in coins:
        for i in range(coin,target+1):
            ways[i] += ways[i-coin]
    return ways[target]

def prob34():
    #digit factorials
    #
    #this one is trivial, because https://en.wikipedia.org/wiki/Factorion
    #tells us only 145 and 40585 are factorions (excluding 1 and 2 as per problem definition)
    #But let's pretend Wikipedia didn't tell us about it.

    limit = 1854721 #aka 9!*6 because explanation on wikipedia
    return sum(i for i in range(10,limit+1) if i == utils.sumOfFactorialDigits(i))

def prob35():
    #circular primes
    limit = int(10e5)
    candidates = [str(x) for x in range(limit) if all(char in '1379' for char in str(x)) and utils.isPrime(x)]
    circulars = set()
    for cand in candidates:
        if utils.isCircularPrime(cand): 
            #we could optimize by adding all cyclic permutations when we find one
            #and avoid testing for all permutations, since we know all of them are
            #circular primes.
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

def prob37():
    #truncable primes
    limit = int(10e5) #rough guess, for all we know the 11th could be the last mersenne prime found.
    lst = []
    candidates = [str(x) for x in range(10,limit) 
        if all(char in '1379' for char in str(x))
        and utils.isPrime(x)]

    for cand in candidates:
        if utils.isTruncablePrime(cand):
            lst.append(int(cand))
    assert len(lst) == 9
    #if we pass the assert, we win
    return sum(lst) + 23 + 53 #those where not in the candidates

def prob39():

    # If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
    # there are exactly three solutions for p = 120.
    # {20,48,52}, {24,45,51}, {30,40,50}
    # For which value of p ≤ 1000, is the number of solutions maximised?

    limit = 1000
    maxP = 0
    maxSols = 0
    for p in range(1,limit+1):
        nbSols = 0
        for a in range(1,limit):
            if p*(p-2*a) % 2*(p-a) == 0: #this division must be an integer
                nbSols += 1
        if nbSols > maxSols:
            maxSols = nbSols
            maxP = p
    return maxP
def prob40():
    #someone's constant
    #created by contataining all positive integers
    from functools import reduce
    from operator import mul
    s = "".join(str(x) for x in (i for i in range(1000000)))
    prod = s[1]+s[10]+s[100]+s[1000]+s[10000]+s[100000]+s[1000000]
    return reduce(mul,(int(x) for x in prod))