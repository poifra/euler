import math
import utils

def prob21():
    #amicable numbers
    numbers = []
    limit = 10000

    for a in range(2,limit):
        b = utils.sumOfDivisors(a)
        if b<a and utils.sumOfDivisors(b) == a:
            numbers.append(a)
            numbers.append(b)

    return sum(numbers)

def prob22():
    #names scores, the solution I wrote is MIA and I cant bother redoing it.
    #It's not a hard problem anyway
    pass

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
    seqLen = 0
    maxI = 0
    for i in range(1,limit):
        if seqLen >= i:
            break

        seen = [0]*(i+1)
        value = 1
        pos = 0
        while seen[value] == 0 and value != 0: #while we havent seen the current value and there's a remainder
            seen[value] = pos
            value *= 10
            value %= i
            pos += 1
        if pos - seen[value] > seqLen:
            seqLen = pos - seen[value]
            maxI = i
    return maxI


def prob27():
    # Considering quadratics of the form:

    # p(n) = n² + an + b, where |a| < 1000 and |b| < 1000

    # Find the product of the coefficients, a and b, 
    # for the quadratic expression that produces 
    # the maximum number of primes for consecutive values of n, starting with n = 0.
    
    #b has to be prime, since our equation must hold for n=0
    limit = 1000
    maxN = maxA = maxB = 0
    primes = utils.genPrimes(limit)
    for a in range(-limit+1,limit+1,2): #a must be odd
        for b in primes:
            n = 1 #we know p(n) for n=0 is prime, so our function already generates at least 1 prime
            while n**2+a*n+b > 0 and utils.isPrime(n**2+a*n+b):
                n += 1
            if n > maxN:
                maxN = n
                maxA = a
                maxB = b
    return maxA*maxB

def prob28():
    #number spiral diagonals
    #trough pen n' paper analysis, we see that the sum of the corners follow 
    #a quadratic progression. Once sovled,
    #it gives us the polynomial 4n² − 6n + 6
    limit = 1001 
    return sum(4*i**2 - 6*i + 6 for i in range(3,limit+1,2)) + 1

def prob29():
    #distinct powers
    limit = 100
    nums = set()
    for a in range(2,limit+1):
        for b in range(2,limit+1):
            nums.add(a**b) #since we use a set we wont add duplicates
    return len(nums)

def prob30():
    #sum of fifth powers
    #we estimate an upper bound to be 6*(9**5) since 5*9**5 has 6 digits.
    limit = 6*9**5
    lst = []
    for i in range(10,limit):
        s = str(i)
        temp = 0
        for char in s:
            temp += int(char)**5
        if temp == i:
            print(i)
            lst.append(i)
    return sum(lst)

if __name__=='__main__':
    import time

    start = time.time()
    print("prob 21",prob21())
    print("Time taken for prob 21",time.time()-start)

    start = time.time()
    print("prob 22",prob22())
    print("Time taken for prob 22",time.time()-start)

    start = time.time()
    print("prob 23",prob23())
    print("Time taken for prob 23",time.time()-start)

    start = time.time()
    print("prob 24",prob24())
    print("Time taken for prob 24",time.time()-start)

    start = time.time()
    print("prob 25",prob25())
    print("Time taken for prob 25",time.time()-start)

    start = time.time()
    print("prob 26",prob26())
    print("Time taken for prob 26",time.time()-start)

    start = time.time()
    print("prob 27",prob26())
    print("Time taken for prob 27",time.time()-start)

    start = time.time()
    print("prob 28",prob28())
    print("Time taken for prob 28",time.time()-start)

    start = time.time()
    print("prob 29",prob29())
    print("Time taken for prob 29",time.time()-start)

    start = time.time()
    print("prob 30",prob30())
    print("Time taken for prob 30",time.time()-start)