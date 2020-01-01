# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

while True:
	a = float(input('Enter first number: '))
	b = float(input('Enter second number: '))
	opr = input('Enter operator[+,=,*,/]')

	if a==45 and b==3 and opr=='*':
		print(555)
	elif a==56 and b==9 and opr=='+':
		print(77)
	elif a==56 and b==6 and opr=='/':
		print(4)

	elif opr == '+':
		print(a+b)
	elif opr == '-':
		print(a-b)
	elif opr == '*':
		print(a*b)
	elif opr == '/':
		print(a/b)