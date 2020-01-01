# File IO Basics

'''

`r` - Open file for reading (default)
`w` - Open a file for writing
`x` - Creates file if does not exist
`a` - Add more content to a file
`t` - Text mode (default)
`b` - Binary mode
`+` - Read and write

'''

# Question of the day:
# Q. How to access docstring of a function
# Ans. function().__doc__

def funcname(parameter_list):
    '''This is a DocString'''
    pass

print(funcname.__doc__)