# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *
  
n = int(input('Enter number of lines: '))
order = int(input('Order Ascending/Descending [1/0] : '))


if order == 1:
    i = 1
    while i <= n:
        print("*"*i)
        i += 1
elif order == 0:
    i = 0
    while i <= n:
        print("*"*(n-i))
        i +=1