class Student():
    pass

harry = Student()
larry = Student()

harry.name = "Harry"
harry.std = "XII"
harry.section = "C"
harry.subjects  = ['physics', 'chemistry', 'maths']

larry.name = "Larry"
larry.std = "XI"
larry.section = "A"

print(harry, larry)
print(harry.name, larry.name)
print(harry.subjects)
# print(larry.subjects)