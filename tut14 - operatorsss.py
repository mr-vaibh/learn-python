''' Operators:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
'''

# Arimthemetic Operators
print('5 + 6 is', 5+6)
print('5 - 6 is', 5-6)
print('5 * 6 is', 5*6)
print('5 / 6 is', 5/6)
print('5 ** 6 is', 5**6)
print('5 // 6 is', 5//6)
print('5 % 6 is', 5%6)

# Assignment Operators
x = 5

x += 7
x -= 7
x *= 7
x /= 7
x **= 7
x //= 7
x %= 7
print(x)

# Comparison Operator
i = 8
print(i == 5)
print(i != 5)
print(i < 5)
print(i > 5)
print(i <= 5)
print(i >= 5)

# Logical Operators (and , or) (&, |)
a = True
b = False

print(a and b)
print(a or b)
print(a and a)
print(a or a)
print(b and b)
print(b or b)

# Identity Operators (is, is not)
x = True
y = False

print(x is y)
print(x is not y)
print(x is x)
print(x is not x)
print(y is y)
print(y is not y)

# Membership Operators (not in)
list = [1, 3, 3, 2, 39, 57, 54]
print(32 in list)
print(32 not in list)
print(2 in list)
print(True in list)  # True is taken as 1, and 1 is present in list
print(False in list)  # False is taken as 0, and 0 is not present in list

# Bitwise Operators
''' Binary data
0 => 00
1 => 01
2 => 10
3 => 11 
'''

print(0 & 1)
print(0 | 1)

print(0 | 3)
'''
   0   => 00
 + 3   => 11
  -----------
   0|3  =>11
'''
print(1 & 2)
print(1 | 2)