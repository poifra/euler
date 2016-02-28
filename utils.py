import math

def genPrimes(n):
	'''
	Implementation of the sieve of Eratosthenes to find all primes below n.
	'''
	l = [i for i in range(1,n,2)]
	for x in range(2,int(math.sqrt(n))):
		l = list(filter(lambda d: d%x != 0 or d == x, l))
	return sorted(l)

def primeFactors(val):
	'''
	Returns the non-distinct prime factors of val
	'''
	for k in range(2, val): 
		if (val % k == 0):
			i = int(val / k) 
			return [k] + primeFactors(i) 
	return [val]

def fact(n):
	'''
	Finds the factors of n.
	'''
	divs = []
	for x in range(1,int(math.sqrt(n))):
		if n%x == 0:
			divs.append(x)
			divs.append(n//x)
	divs.sort()
	return divs

def collatz(n):
	'''
	Returns the Collatz sequence starting with n.
	'''
	lst = []
	lst.append(n)
	k = n
	while k != 1:
		if k % 2 == 0:
			lst.append(k//2)
		else:
			lst.append(3*k+1)
		k = lst[-1]
	return lst

def sumOfDigits(n):
	'''
	Returns the sum of digits in an integer n
	'''
	s = 0
	while n:
		s += n % 10 #get last digit
		n //= 10 #remove it
	return s