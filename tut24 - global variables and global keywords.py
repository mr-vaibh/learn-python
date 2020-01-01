l = 5   # Global variable --> Module level

def func(n):
	l = 11   # Local variable --> Block level scope, like `let/const in JS`
	''' first l will be searched in local block, and if `l` is not found then it will search globally
	if there would no l=5, global l would have been used 
	in case if global `l` is retrieved in func(), you can't change it's value
	it can only be readed (read only variable)
	'''
	l += 5
	m = 8
	print(l, 'I have printed', n)

func('some text')

print(l**2)
# print(m)  will throw error as `m` is a local variable inside func()


x = 3
def tom():
	x = 20
	def jerry():
		global x
		x = 88
	print('before calling jerry()', x)
	jerry()
	print('after calling jerry()', x)

tom()

print(x)
