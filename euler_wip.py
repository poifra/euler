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

def prob96():
    #sudoku solving
    #this is old code, so the style might be different
    #tbe solver is basically an unoptimized tree search 
    #(ie it doesnt check for squares where only 1 number is possible)
    #we define a bunch of methods
    #to help us validate and load the file
    import sys
    size = 9

    def ppSudokuMat(config):
        for i in range(size):
            if(i % 3 == 0):
                print ("|-----------------------|") 
            for j in range(size):
                if(j % 3 == 0):
                    print ("| ",end='')
                print (str(config[i][j])+" ",end='')
            print ("|\n",end='')
        print ("-------------------------") 

    def readConfigs(filename):
        allConfigs = []
        allLines = []
        with open(filename, 'r') as confs:
            allLines = confs.read().split('\n')

        for line in allLines:
            i = j = 0
            aConfig = [[0]*size for _ in range(size)]
            for x in line:
                aConfig[i][j] = int(x) #fill the matrix column by column
                j += 1
                if(j % size == 0):
                    i += 1
                    j = 0
            allConfigs.append(aConfig)

        return allConfigs

    def getPossibleNumbers(config,line,col):
        possibleNumbers = [1,2,3,4,5,6,7,8,9]
        
        for i in range(size):
            x = config[line][i]
            if(x in possibleNumbers):
                possibleNumbers.remove(x)
                
        for i in range(size):
            x = config[i][col]
            if(x in possibleNumbers):
                possibleNumbers.remove(x)
        
        hBox = col - col % 3
        vBox = line - line % 3
        
        for i in range(3):
            for j in range(3):
                x = config[i+vBox][j+hBox]
                if(x in possibleNumbers):
                    possibleNumbers.remove(x)
                    
        return possibleNumbers
        
    def depthFirst(config):
        sys.setrecursionlimit(1000)
        complete = True
        i = j = 0
        
        #check for a 0 in the matrix. This also gives us the i,j coordinates of the first 0 we find
        while(complete and j < size and i < size): 
            complete = config[i][j] != 0
            if(complete):
                i += 1
                if(i % size == 0):
                    j += 1
                    i = 0
        if(complete):
            return True
            
        possibleNumbers = getPossibleNumbers(config,i,j)
     #   print("possibilites for",i,j,possibleNumbers)
        if(possibleNumbers == []):
            return False
        for n in possibleNumbers:
            config[i][j] = n
            if(depthFirst(config)==True):
                return True
            config[i][j] = 0
                                      
        return False

    confs = readConfigs('prob96text.txt')
    numbers = []
    for c in confs:
        depthFirst(c)
        numbers.append(int("".join(map(str,c[0][:3])))) #this captures the first tree numbers of each solution
        ppSudokuMat(c)
    return sum(numbers)

def prob97():
    '''
    The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; 
    it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p−1, have been found which contain more digits.
    However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.
    Find the last ten digits of this prime number.
    '''
    return (28433*int('1'+'0'*7830457,2)+1) % 10000000000
