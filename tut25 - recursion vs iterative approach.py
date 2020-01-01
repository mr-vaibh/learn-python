# n! = n*(n-1)*(n-2)*(n-3)...3*2*1
# n! = n*(n-1)!

# Iterative Approach
def factorial(n):
	'''
	:param n: Integer
	:return: n*(n-1)*(n-2)*(n-3)...3*2*1
	'''
	fac = 1
	for i in range(1, n+1):
		fac *= i
	return fac

num = int(input('Enter any whole number: '))
print(factorial(num))


# Recursive Approach
def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)
	'''
	Logic : (let input be 5)
	5 * fact(4)
	5 * 4 * fact(3)
	5 * 4 * 3 * fact(2)
	5 * 4 * 3 * 2 * fact(1)
	5 * 4 * 3 * 2 * 1 = 120        (if n==1: return 1)
	'''

num = int(input('Enter any whole number: '))
print(fact(num))


'''
we can make this even shorter ;)
def fact(n):
	return 1 if n==1 else n*fact(n-1)

(above code is right)
'''



# Fibonacci Series

# 0 1 1 2 5 8 13...n
num = int(input('Enter a natural number: '))

i = 0
def fibonacci(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(num))