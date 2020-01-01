s = set()
print(s)

# s = set(1, 2, 3, 4, 5) ----> Wrong !!
s = set([1, 2, 3, 4, 5, 10]) # ----> Right :)

# print(type(s))

l = [1, 2, 3, 4, 4]

setFromList = set(l)
print(setFromList)
print(type(setFromList))

print(len(s))
print(min(s))
print(max(s))

s.add(6)
s.remove(10)
print(s)

newSet = {2, 3, 45, 'hello cool dudes'}
s.union(newSet)
s.intersection(newSet)

s_newSet_union = s.union(newSet)
s_newSet_intersection = s.intersection(newSet)
s_newSet_difference = s.difference(newSet)

print(s_newSet_union)
print(s_newSet_intersection)
print(s_newSet_difference)

print(s.isdisjoint(newSet))

''' Remember,    True === 1
				False === 0
if you add True or False in a set
and there is 1 or 0 already present in the set
then True or False would be skipped


Because in Python 1 == True (and hash(1) == hash(True)) and you have 1 in your set already.

Imagine this example:

example1 = {0, False, None}
example2 = {1, True}

print(example1)
print(example2)
Will output:

{0, None}
{1}
First set has 0 and None because 0 == False but 0 != None. With second set 1 == True so True isn't added to the set.

Proof :
https://stackoverflow.com/questions/51505826/how-come-i-can-add-the-boolean-value-false-but-not-true-in-a-set-in-python
'''