list1 = [ ["Harry", 1], ["Larry", 2], ["Carry", 6], ["Marie", 250]]
dict1 = dict(list1)
print(dict1)

for item in dict1:
	print(item)


for item, key in dict1.items():
	print(item, "has key ", key)

items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

# .isnumeric() function to check if the variable is numeric or not
for item in items:
	if str(item).isnumeric() and item>=6:
		print(item)

