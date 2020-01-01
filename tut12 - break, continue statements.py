i = 0

while True:
	if i+1<5:
		continue   # will jump to next iteration (next value of i)
	
	print(i+1)
	if i==44:
		break   # will break the loop (will jump to line 12)
	
	i += 1
print('loop ended')


while 1:
	inp = int(input('Enter a number'))
	if inp > 100:
		break
	else:
		print('Try again\n')
		continue