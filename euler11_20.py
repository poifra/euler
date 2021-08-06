import utils
import math

def prob11():
    grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
    [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
    [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
    [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
    [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
    [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
    [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
    [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
    [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
    size = 20
    temp = 0
    #horizontal
    for x in range(size - 4):
        for y in range(size):
            res = grid[x][y] * grid[x + 1][y] * grid[x + 2][y] * grid[x + 3][y]
            if res > temp:
                temp = res
    #vertical
    for x in range(size):
        for y in range(size - 4):
            res = grid[x][y] * grid[x][y + 1] * grid[x][y + 2] * grid[x][y + 3]
            if res > temp:
                temp = res

    #diagonal, going left to right
    for x in range(size - 4):
        for y in range(size - 4):
            res = grid[x][y] * grid[x + 1][y + 1] * grid[x + 2][y + 2] * grid[x + 3][y + 3]
            if res > temp:
                temp = res

    #diagonal, going right to left
    for x in range(size - 4):
        for y in range(3,size):
            res = grid[x][y] * grid[x + 1][y - 1] * grid[x + 2][y - 2] * grid[x + 3][y - 3]
            if res > temp:
                temp = res

    return temp

def prob12():
    limit = 500
    nbDiv = 0
    i = 1
    while nbDiv < limit:
        triangular = (i * (i + 1)) / 2
        nbDiv = len(utils.fact(triangular))
        i+=1
    return triangular

def prob13():
    with open('prob13text.txt','r') as f:
        data = f.read().split('\n')
        data = data[:len(data) - 1] #remove last split, which is NaN.
        s = 0
        for nbr in data:
            s+= int(nbr)
        return str(s)[:10]

def prob14():
    limit = 1000000
    longest = []
    for i in range(1,limit):
        res = utils.collatz(i)
        if len(res) > len(longest):
            longest = res
    return longest[0]

def prob15():
    '''
    The number of lattice paths between (0,0) and (x,y) is 
    the binomial coefficient 
    ( x+y ) 
    (  x  )
    =
    (x+y)! / (x!*y!)
    '''
    x = 20
    y = 20
    return math.factorial(x + y) / (math.factorial(x) * math.factorial(y))

def prob16():
    s = str(2 ** 1000)
    return sum([int(i) for i in s])


def prob17():
    numbers = [0] * 1001

    numbers[1:21] = map(len,["one","two","three","four","five","siz","seven","eight","nine","ten",
        "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"])
    numbers[30] = len("thirty")
    numbers[40] = len("forty")
    numbers[60] = len("sixty")
    numbers[50] = len("fifty")
    numbers[60] = len("sixty")
    numbers[70] = len("seventy")
    numbers[80] = len("eighty")
    numbers[90] = len("ninety")

    for i in range(len(numbers)):
        temp = i
        if not numbers[temp]:
            if temp // 1000:
                numbers[i] += numbers[temp // 1000] + len("thousand")
                temp = temp - (1000 * (temp // 1000))
            if temp // 100:
                numbers[i] += numbers[temp // 100] + len("hundred")
                temp = temp - (100 * (temp // 100))
                if temp > 0:
                    numbers[i] += len("and")
            if temp <= 20 or temp % 10 == 0:
                numbers[i] += numbers[temp]
            else:
                numbers[i] += numbers[temp - (temp % 10)]
                numbers[i] += numbers[temp - (10 * (temp // 10))]

    return sum(numbers)

def prob18():
    # maximum path I
    # dynamic programming is a better idea, but this will wait until prob 67
    # which is the same as this
    # but unsolvable by brute force
    with open('prob18text.txt','r') as f:
        size = 15
        data = f.read().split('\n')
        lst = [[] * size] * size
        for i,line in enumerate(data):
            numbers = line.split(' ')
            lst[i] = list(map(int,numbers)) + [0] * (size - len(numbers))

        highest = 0
        possiblePaths = 2 ** (len(lst) - 1)
        #since we have two choices at each level, we can represent the path as
        #a binary string.
        for i in range(possiblePaths):
            temp = lst[0][0]
            index = 0
            for j in range(len(lst) - 1):
                index = index + (i >> j & 1)
                temp += lst[j + 1][index]
            if temp > highest:
                highest = temp
        return highest

def prob19():
    #how many sundays
    from datetime import date
    count = 0
    for year in range(1901,2001):
        for month in range(1,13):
            d = date(year,month,1)
            if d.weekday() == 6:
                count += 1
    return count

def prob20():
    return utils.sumOfDigits(math.factorial(100))

def launch():
    import time

    start = time.time()
    print("prob 11",prob11())
    print("Time taken for prob 11",time.time() - start)

    start = time.time()
    print("prob 12",prob12())
    print("Time taken for prob 12",time.time() - start)

    start = time.time()
    print("prob 13",prob13())
    print("Time taken for prob 13",time.time() - start)

    start = time.time()
    print("prob 14",prob14())
    print("Time taken for prob 14",time.time() - start)

    start = time.time()
    print("prob 15",prob15())
    print("Time taken for prob 15",time.time() - start)

    start = time.time()
    print("prob 16",prob16())
    print("Time taken for prob 16",time.time() - start)

    start = time.time()
    print("prob 17",prob16())
    print("Time taken for prob 17",time.time() - start)

    start = time.time()
    print("prob 18",prob18())
    print("Time taken for prob 18",time.time() - start)

    start = time.time()
    print("prob 19",prob19())
    print("Time taken for prob 19",time.time() - start)

    start = time.time()
    print("prob 20",prob20())
    print("Time taken for prob 20",time.time() - start)
