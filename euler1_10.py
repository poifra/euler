import utils
import math

def prob1():
    limit = 1000
    return sum([i for i in range(limit) if i % 3 == 0 or i % 5 == 0])

def prob2():
    limit = 4000000
    s = 0
    a = 1
    b = 1
    c = a + b
    while c < limit:
        s += c
        a = b + c
        b = c + a
        c = a + b
    return s

def prob3():
    return utils.prime_factors(600851475143)[-1::]

def prob4():
    def isPal(n):
        s = str(n)
        return s[::-1] == s
    max = 0
    for i in range(100,1000):
        for j in range(i,1000):
            res = i*j
            if isPal(res) and res > maxPal:
                maxPal = res
    return maxPal

def prob5():
    k = 20 #limit
    N = 1 #product
    i = 0
    check = True
    limit = math.sqrt(k)
    p = utils.genPrimes(k)
    for prime in p:
        a_i = 1
        if check:
            if prime <= limit:
                a_i = math.floor(math.log(k) / math.log(prime))
            else: # at this point, we know we must mutiply all primes
                check = False
        N *= prime ** a_i
    return N

def prob6():
    value = 100
    sumOfSquares = (value*(value+1)*(2*value+1))/6
    sumSquared = ((value*(value+1))/2)**2
    print("sum of squares",sumOfSquares)
    print("sum squared",sumSquared)
    return sumSquared - sumOfSquares

def prob7():
    target = 10001
    primeCount = 0
    i = 0
    while primeCount < target:
        if utils.isPrime(i):
            primeCount += 1
        i += 1
    return i-1

def prob8():
    n = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
""".replace('\n','')
    print(int(n))

def prob9():
    #bruteforce ftw
    for a in range(1, 1000):
        for b in range(a, 1000):
            for c in range(b, 1000):
                if a**2 + b**2 == c**2 and a+b+c == 1000:
                    return a*b*c
    return -1

if __name__=='__main__':
    import time

    start = time.time()
    print("prob 1",prob1())
    print("Time taken for prob 1",time.time()-start)

    start = time.time()
    print("prob 2",prob2())
    print("Time taken for prob 2",time.time()-start)

    start = time.time()
    print("prob 3",prob3())
    print("Time taken for prob 3",time.time()-start)

    start = time.time()
    print("prob 4",prob4())
    print("Time taken for prob 4",time.time()-start)

    start = time.time()
    print("prob 5",prob5())
    print("Time taken for prob 5",time.time()-start)

    start = time.time()
    print("prob 9",prob9())
    print("Time taken for prob 9",time.time()-start)
