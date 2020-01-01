class Employee:
    no_of_leaves = 8

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 4500000
harry.designation = "Senior Software Developer"
print(harry.__dict__)    # returns the dictionary of all user created instances and its values of harry

rohan.name = "Rohan"
rohan.salary = 1500000
rohan.designation = "Junior Developer"
print(rohan.__dict__)    # returns the dictionary of all user created instances and its values of rohan

# no_of_leaves is not in __dict__ as it is an inherited key from Employee()
print(rohan.no_of_leaves)  # changing instance variable
rohan.no_of_leaves = 11   # now it is not inherited from Employee(), changing its value creates a new instance for rohan

# To change no_if_leaves for all objects use className.attribute = data
Employee.no_of_leaves = 10   # changing class variable
print(Employee.no_of_leaves)

print(Employee.__dict__)
