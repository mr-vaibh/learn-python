class Employee():
    no_of_leaves = 8  # it is set for all employees

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation

    def details(self):
        return f'Name: {self.name}\nSalary: {self.salary}\nDesignation: {self.designation}\nNumber of leaves: {self.no_of_leaves}\n'

harry = Employee('Harry', 4500000, 'Senior Software Developer')
rohan = Employee('Rohan', 1500000, 'Junior Developer')

'''We will use __init__() method as a constructor to create objects'''
# harry.name = 'Harry'
# harry.salary = 4500000
# harry.designation = 'Senior Software Developer'

# rohan.name = 'Rohan'
# rohan.salary = 1500000
# rohan.designation = 'Junior Developer'


print(harry.details())
print(rohan.details())

# no matter if you have not added any parameter, 1 parameter (self object) always get passed into class method by default
# if you have to verify it, remove self param from details() method of Employee class
