import time, math

s=  time.time()

def IsPrime( n ):
	if n == 2:
		return 1
	elif n % 2 == 0:
		return 0
	i = 3
	limit = int( math.sqrt(n) ) + 1
	while( i < limit ):
		if ( n % i == 0):
			return 0
		i += 1
	return 1

N,T = 1,3

while N < 10001:
	print N
	print T
	if IsPrime(T):
		N+=1
	T+=2
print T-2
print time.time() -s


