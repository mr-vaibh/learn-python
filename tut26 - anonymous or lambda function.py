# Lambda functions or anonymous functions

# Syntax --> lambda parameter_list: expression

# def add(a, b):
# 	return a + b

add = lambda a, b: a + b

print(add(2, 5))

def a_first(x):
	return x[0]

a = [[1,14], [5,6], [8,45]]
# a.sort(key=a_first)
a.sort(key=lambda x: x[0])

print(a)