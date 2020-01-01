class Employee():
    no_of_leaves = 8

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
    
    def details(self):
        return f'Name: {self.name}\nSalary: {self.salary}\nDesignation: {self.designation}\nNumber of leaves: {self.no_of_leaves}'
    
    @classmethod  # built-in classmethod decorators
    def changeLeaves(cls, newleaves):  # cls means class (passing whole class as parameter)
        cls.no_of_leaves = newleaves


harry = Employee('Harry', 4500000, 'Senior Software Developer')
rohan = Employee('Rohan', 1500000, 'Junior Developer')

print(harry.details())

# Class Variable
print(Employee.no_of_leaves)

# Instance Variable
''' First it will check for a local/instance variable
if it doesn't exists, then it will check for class instance '''
print(rohan.no_of_leaves)

rohan.changeLeaves(10)
print(rohan.no_of_leaves)


# https://youtu.be/16K7DvU5Bvw?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&t=139
# at 2:20
