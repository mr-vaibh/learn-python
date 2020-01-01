
def printHar(string):
    return f'give this string to harry{string}'

def add(a, b):
    return a + b +5


# If the program is itself executed
# then __name__ will me __main__

print('and the name is', __name__)

if __name__ == "__main__":
    print(printHar('Harry1'))

    o = add(4, 6)
    print(o)
