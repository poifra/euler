import utils
import math

def compute_slow(N: int) -> int:
    debug_sums = {}
    my_sums = {}
    half_power_of_two = 1
    power_of_two = 1

    for _ in range(int(math.log(N, 2)) + 1):
        power_of_two *= 2
        for number in range(half_power_of_two, N + 1):
            remainder = number % power_of_two
            factor_left = abs(half_power_of_two - remainder - 1) + half_power_of_two
            factor_right = number // power_of_two
            summand_after = 0
            if remainder >= half_power_of_two:
                summand_after = 2 * (remainder - half_power_of_two + 1)
            value = factor_left * factor_right + summand_after
            debug_sums[half_power_of_two] = debug_sums.get(half_power_of_two, {})
            debug_sums[half_power_of_two][remainder] = debug_sums[half_power_of_two].get(remainder, [])
            debug_sums[half_power_of_two][remainder].append(value)
            my_sums[half_power_of_two] = my_sums.get(half_power_of_two, 0) + value
        half_power_of_two = power_of_two
    corrected = {factor: factor * value for factor, value in my_sums.items() if isinstance(factor, int)}
    result = 2 * sum(corrected.values())
    return result

def prob67():
    '''
    max sum II, non bruteforce edition
    This is the same as prob 18, but with a much bigger scale.
    This time we use dynamic programming, we add up maximums, starting from the bottom of the triangle.
    '''
    highest = 0
    size = 100
    lst = [[] * size] * size
    with open('prob67text.txt','r') as f:
        data = f.read().split('\n')
        for i,line in enumerate(data):
            numbers = line.split(' ')
            lst[i] = list(map(int,numbers)) + [0] * (size - len(numbers))

    for i in range(size - 2, -1, -1):
        for j in range(i + 1):
            lst[i][j] += max(lst[i + 1][j],lst[i + 1][j + 1])
    return lst[0][0]


def prob92():
    limit = int(1e7)
    count = 0
    for i in range(1,limit):
        n = i
        while n != 1 and n != 89:
            n = sum(int(k) ** 2 for k in list(str(n)))
        if n == 1:
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
                print("|-----------------------|") 
            for j in range(size):
                if(j % 3 == 0):
                    print("| ",end='')
                print(str(config[i][j]) + " ",end='')
            print("|\n",end='')
        print("-------------------------") 

    def readConfigs(filename):
        allConfigs = []
        allLines = []
        with open(filename, 'r') as confs:
            allLines = confs.read().split('\n')

        for line in allLines:
            i = j = 0
            aConfig = [[0] * size for _ in range(size)]
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
                x = config[i + vBox][j + hBox]
                if(x in possibleNumbers):
                    possibleNumbers.remove(x)
                    
        return possibleNumbers
        
    def depthFirst(config):
        sys.setrecursionlimit(1000)
        complete = True
        i = j = 0
        
        #check for a 0 in the matrix.  This also gives us the i,j coordinates
        #of the first 0 we find
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
            if(depthFirst(config) == True):
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
    return (28433 * int('1' + '0' * 7830457,2) + 1) % 10000000000
