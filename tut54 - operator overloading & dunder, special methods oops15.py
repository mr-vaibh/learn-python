class Employee():
    no_of_leaves = 8

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
    
    def printDetails(self):
        return f'Name: {self.name}\nSalary: {self.salary}\nDesignation: {self.designation}\nNumber of leaves: {self.no_of_leaves}'
    
    @classmethod
    def changeLeaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    
    # this method will run when we use `+` operator anywhere
    def __add__(self, other):
        return self.salary + other.salary  # its not necessary to only add, we can perform any function
    
    # this method will run when we use `/` operator
    def __truediv__(self, other):
        return self.salary / other.salary
    
    # this method will run when print(repr()) function is used
    def __repr__(self):
        return f'Employee({self.name}, {self.salary}, {self.designation})'
    
    # this method will run when print(str()) function is used
    def __str__(self):
        return f'Name: {self.name}\nSalary: {self.salary}\nDesignation: {self.designation}\nNumber of leaves: {self.no_of_leaves}'

emp1 = Employee('Harry', 450000, 'Programmer')
emp2 = Employee('Rohan', 25000, 'Cleaner')

print(emp1 + emp2)
print(emp1 / emp2)
print(repr(emp1))
print(str(emp1))


''' For more goto -
`Mapping Operators to Functions` section at
https://docs.python.org/3/library/operator.html

'''