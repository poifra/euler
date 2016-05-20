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
	c = a+b
	while c < limit:
		s+=c
		a = b+c
		b = c+a
		c = a+b
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
	for i in range(len(p)):
		a_i = 1
		if check:
			if p[i] <= limit:
				a_i = math.floor(math.log(k) / math.log(p[i]))
			else: # at this point, we know we must mutiply all primes
				check = False
		N *= p[i] ** a_i
	return N

def prob9():
	for a in range(1,1000):
		for b in range(a,1000):
			for c in range(b,1000):
				if a**2 + b**2 == c**2 and a+b+c == 1000:
					return a*b*c
	return -1

def prob11():
	grid = [
	[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
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
	for x in range(size-4):
		for y in range(size):
			res = grid[x][y]*grid[x+1][y]*grid[x+2][y]*grid[x+3][y]
			if res > temp:
				temp = res
	#vertical
	for x in range(size):
		for y in range(size-4):
			res = grid[x][y]*grid[x][y+1]*grid[x][y+2]*grid[x][y+3]
			if res > temp:
				temp = res

	#diagonal, going left to right
	for x in range(size-4):
		for y in range(size-4):
			res = grid[x][y]*grid[x+1][y+1]*grid[x+2][y+2]*grid[x+3][y+3]
			if res > temp:
				temp = res

	#diagonal, going right to left
	for x in range(size-4):
		for y in range(3,size):
			res = grid[x][y]*grid[x+1][y-1]*grid[x+2][y-2]*grid[x+3][y-3]
			if res > temp:
				temp = res

	return temp

def prob12():
	limit = 500
	nbDiv = 0
	i = 1
	while nbDiv < limit:
		triangular = (i * (i+1))/2
		nbDiv = len(utils.fact(triangular))
		i+=1
	return triangular

def prob13():
	with open('prob13text.txt','r') as f:
		data = f.read().split('\n')
		data = data[:len(data)-1] #remove last split, which is NaN.
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
	return math.factorial(x+y)/(math.factorial(x)*math.factorial(y))

def prob16():
	s = str(2**1000)
	return sum([int(i) for i in s])


def prob17():
	numbers =  [0] * 1001

	numbers[1:21] = map(len,["one","two","three","four","five","siz","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"])
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
				temp = temp - (1000*(temp // 1000))
			if temp // 100:
				numbers[i] += numbers[temp // 100] + len("hundred")
				temp = temp - (100*(temp//100))
				if temp > 0:
					numbers[i] += len("and")
			if temp <= 20 or temp % 10 == 0:
				numbers[i] += numbers[temp]
			else:
				numbers[i] += numbers[temp - (temp%10)]
				numbers[i] += numbers[temp - (10*(temp//10))]

	return sum(numbers)

def prob18():
	#maximum path I
	with open('prob18text.txt','r') as f:
		size = 15
		data = f.read().split('\n')
		lst = [[]*size]*size
		i = 0
		for line in data:
			lst[i] = list(map(int, line.split(' ')))
			i+=1
		m = 0
		
		return m

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
	#non-abundant sums
	#according to magic, erm, maths, all numbers > 28123 can be written as a sum of two abundant numbers.
	#we are looking for the sum of all numbers that cannot be written as such a sum.
	limit = 28123
	is_a_sum = [False]*(limit+1)
	abundant = []
	for i in range(12,limit+1):
		if utils.sumOfDivisors(i) > i:
			abundant.append(i)

	for i in range(len(abundant)):
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
	limit = 1000
	a = b = i = 1
	while len(str(a)) < limit:
		a,b=b,a+b
		i+=1
	return i