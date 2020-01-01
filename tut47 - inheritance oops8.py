class Employee():
    no_of_leaves = 8

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
    
    def employeeDetails(self):
        return f'Name: {self.name}\nSalary: {self.salary}\nDesignation: {self.designation}\nNumber of leaves: {self.no_of_leaves}'
    
    def annualSalary(self):
        return int(self.salary)*12
    
    @classmethod
    def changeLeaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    
    @staticmethod   # method which doesn't take self or cls as a parameter, just perform defined function
    def greet(string):
        return f'Hello! ' + string

class Programmer(Employee):
    def __init__(self, name, salary, designation, languages, github):
        self.name = name
        self.salary = salary
        self.designation = designation
        self.languages = languages
        self.github = github
    
    def programmerDetails(self):
        return f'Name: {self.name}\nSalary: {self.salary}\nDesignation: {self.designation}\nLanguage: {self.languages}\nGithub: {self.github}\nNumber of leaves: {self.no_of_leaves}\n'

harry = Employee('Harry', '4500000', 'Senior Software Developer')
rohan = Employee('Rohan', '1500000', 'Junior Developer')

skillF = Programmer('SkillF', 500000, 'Senior Developer', ['Python', 'C++'], 'https://github.com/skillf')
print(skillF.programmerDetails())

