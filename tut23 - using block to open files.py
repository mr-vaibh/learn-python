'''
`with as` block do the exact following code :

file = open('file.txt', 'rt')
file.close()

'''

# `with as` do not require close() function
with open('file.txt', 'rt') as file:
	print(file.readlines())
	file.seek(0)
	a = file.read(6)
	print(a)