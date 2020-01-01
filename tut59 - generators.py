
"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration - process

"""

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

h = 'harry'
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)

# We can create single line generators by following method
evens = (i for i in range(100) if i%2==0)
print(evens)
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())

# Iterating evens
for item in evens:
    print(item)

# https://www.youtube.com/watch?v=S9d-fwalZ_Q&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=73
