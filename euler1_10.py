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
