# Built-In function (pre-defined fucntions)

# for eg - sum(param) where param must be an iterable var
# like list, tuple, set
# c = sum((9, 8)) or c = sum([9, 8]) or c = sum({9, 8})

def func():
    print('Hello, u are in function')

func()   # only print the hello statement
print(func())  # print hello statement and return None

# this line will also call function and print the statement
# but if u had only returned the value then the value would have stored in the variable
a = func()

def add(a, b):
    '''This is a function which calculate average of two numbers'''
    return (a+b)/2

x = add(5, 7)
print(x)

print(add.__doc__)   # first multiline comment in a function is a DocString