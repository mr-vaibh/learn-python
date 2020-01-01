''' Read function '''

# file = open('file.txt')
# content = file.read()
# print(content)
# file.close()

# file = open('file.txt', 'r')
# content = file.read()
# print(content)
# file.close()

# file = open('file.txt', 'rt')
# content = file.read()
# print(content)
# file.close()

file = open('file.txt', 'rb')
content = file.read()
print(content)
file.close()



file = open('file.txt', 'r')
content = file.read(3)
print(content)

content = file.read(3)
print(content)

content = file.read(3545)
print(content)
file.close()


file = open('file.txt', 'rt')
content = file.read()         # once we read the file, the pointer gets empty and we can't make new var = file.read()
# Reading text line by line
for line in content:
	print(line, end='')

content2 = file.read()
print(content2)           # see content2 is not null
file.close()

# To prevent this single time read of a file don't use read()
# directly pull var = file

file = open('file.txt')
for line in file:
	print(line, end="")
file.close()


''' Readline function '''

file = open('file.txt', 'rt')
content = file.readline()
print(content)

content = file.readline()
print(content)
file.close()


''' Readlines function '''

file = open('file.txt', 'rt')
content = file.readlines()   # returns list of all lines
print(content)
file.close()

file = open('file.txt', 'rt')
content = file.readlines(1)
print(content)
print(content[0])
file.close()