class Employee():
    no_of_leaves = 8

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
    
    def details(self):
        return f'Name: {self.name}\nSalary: {self.salary}\nDesignation: {self.designation}\nNumber of leaves: {self.no_of_leaves}'
    
    def annualSalary(self):
        return int(self.salary)*12
    
    @classmethod
    def changeLeaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    
    @classmethod
    def constructorFromStr(cls, string):
        return cls(*string.split('--'))
    
    @staticmethod   # method which doesn't take self or cls as a parameter, just perform defined function
    def greet(string):
        return f'Hello! ' + string


harry = Employee.constructorFromStr('Harry--4500000--Senior Software Developer')
rohan = Employee.constructorFromStr('Rohan--1500000--Junior Developer')

print(rohan.details())


# Only theory
# https://www.youtube.com/watch?v=wySW_E4XsvE&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=60