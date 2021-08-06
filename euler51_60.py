def prob52():
    '''
    Permutted multiples
    It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
    '''
    found = False
    i = 1
    while not(found):
        if utils.is_perm(i,2 * i) and utils.is_perm(i,3 * i) and utils.is_perm(i,4 * i) and utils.is_perm(i,5 * i) and utils.is_perm(i,6 * i):
            return i
        i += 1

def prob53():
    #combinatorics selections
    def combine(n,r):
        from math import factorial as f
        return int((f(n)) / (f(r) * f(n - r)))
    limit = 100
    count = 0
    for n in range(1,limit + 1):
        for r in range(n):
            if combine(n,r) > int(1e6):
                count += 1
    return count

def prob56():
    #powerful digit sums
    maxS = 0
    for a in range(100):
        for b in range(1,100):
            r = a ** b
            s = utils.sumOfDigits(r)
            if s > maxS:
                maxS = s
    return maxS

def prob57():
    p = 1 
    q = 1
    good = 0
    for _ in range(1000):
        newP = p + 2 * q
        newQ = p + q
        if(len(str(newP)) > len(str(newQ))):
           good += 1
        p = newP
        q = newQ
    return good

def prob59():
    from itertools import product
    #we know the key is 3 lowercase characters
    def chunkify(lst,chunkSize):
        for i in range(0, len(lst), chunkSize):
            yield lst[i:i + chunkSize]

    def freqAnalyse(string):
        string = string.lower()
        frequencies = {}
        counts = {}
        for letter in string:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
        for letter in counts.keys():
            frequencies[letter] = counts[letter] / len(string) * 100
        return frequencies

    keyLen = 3
    possibleKeys = list(product([i for i in range(97,123)],repeat=keyLen))
    possibleMessages = {}

    with open('prob59text.txt', 'r') as cipher:
        numbers = list(chunkify(list(map(int,cipher.read().split(','))),3)) #oooh sexy one liners!
  
        for key in possibleKeys:
            outString = ''
            printable = True
            for chunk in numbers:
                if len(chunk) == 1:
                    outString += chr(chunk[0] ^ key[0])
                else:
                    outString += chr(chunk[0] ^ key[0]) + chr(chunk[1] ^ key[1]) + chr(chunk[2] ^ key[2])

            for letter in outString:
                if ord(letter) < 32 or ord(letter) > 127:
                    printable = False
                    break

            if printable:
                possibleMessages["".join(chr(k) for k in key)] = outString #we do this to have a string rep of the key

    #now we need to do a frequency analysis on each possible message
    for key,message in possibleMessages.items():
        freqs = freqAnalyse(message)
        lst = sorted(freqs,key=freqs.get)[::-1]
        if lst[0] == ' ' and lst[1] == 'e':
            print(key, message)

    print(lst)

def prob60():
    import itertools
    combs = itertools.combinations(utils.genPrimes(int(1e5)),5)
    for combo in combs:
        concats = itertools.combinations(combo,2)
        allPrimes = True
        for conc in concats:
            leftRight = int(str(conc[0]) + str(conc[1]))
            rightLeft = int(str(conc[1]) + str(conc[0]))
            if not utils.isPrime(leftRight) or not utils.isPrime(rightLeft):
                allPrimes = False
            if not allPrimes:
                break
        if allPrimes:
            return combo,sum(combo)
