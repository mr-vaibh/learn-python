file1 = open('file.txt')

try:
    file = open('file.txt')
except EOFError as e:
    print('EOFError: ', e)
except IOError as e:
    print('IOError: ', e)
except Exception as e:
    print(e)
else:
    print('This will run only if except is not running')
finally:
    print('It is must to execute the code at the end')
    print('Run this anyway...')
    file.close()
    file1.close()

print('Main file code')