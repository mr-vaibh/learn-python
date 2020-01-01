file = open('file.txt')

# .tell() method returns current position of file object.
print(file.tell())
print(file.readline())

print(file.tell())

# .seek(param) sets the file's current character position at the offset
file.seek(10)
print(file.tell())
print(file.readline())

print(file.tell())

file.seek(0)
print(file.tell())

file.close()