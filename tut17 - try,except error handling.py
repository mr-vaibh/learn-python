a = input('Enter first number: ')
b = input('Enter second number: ')

try:
    print('the sum of two numbers is',
    int(a)+int(b))    # yes, you can break line after a comma in print()
except Exception as e:
    print('Error: ', e)

print('Final line to be executed')