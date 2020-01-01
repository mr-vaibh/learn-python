def function1():
    print('Hello!!')

func2 = function1
del function1

func2()


def funcReturn(num):
    if num==0:
        return print
    if num==1:
        return sum
a = funcReturn(1)
print(a)


def executor(func):
    '''we can pass function in a function
    and also can return function from a function'''

    func('we are inside executor function')

executor(print)


def decorator(func):
    def execute():
        print('Executing...')
        func()
        print('Executed')
    return execute

@decorator
def something():
    print('printing something to understand')

# something = decorator(something)

something()

''' If you are not understanding, goto
https://youtu.be/_zTyBMFD4yY?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&t=494

at 8:50
'''