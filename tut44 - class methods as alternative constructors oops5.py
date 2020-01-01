class Employee():
    no_of_leaves = 8

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
    
    def details(self):
        return f'Name: {self.name}\nSalary: {self.salary}\nDesignation: {self.designation}\nNumber of leaves: {self.no_of_leaves}'
    
    @classmethod  # built-in classmethod decorators
    def changeLeaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    
    @classmethod
    def constructorFromStr(cls, string):
        # params = string.split('--')
        # return cls(params[0], params[1], params[2])
        return cls(*string.split('--'))   # using *args (passing *list created from split string)


# harry = Employee('Harry', 4500000, 'Senior Software Developer')
# rohan = Employee('Rohan', 1500000, 'Junior Developer')

harry = Employee.constructorFromStr('Harry--4500000--Senior Software Developer')
rohan = Employee.constructorFromStr('Rohan--1500000--Junior Developer')

rohan.changeLeaves(10)

print(rohan.details())
