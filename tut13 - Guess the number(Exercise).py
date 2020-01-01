import random

n = random.randrange(1,20)
print(n)

while True:
	user = int(input("Guess the number betwen 1 and 20: "))

	if user>n:
		print('Your guessed number is greater than original number')
	elif user<n:
		print('Your guessed number is smaller than original number')
	elif user == n:
		break

print('Gotcha !! The original number is', user )