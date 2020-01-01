class Employee():
	no_of_leaves = 8

	def __init__(self, name, salary, designation):
		self.name = name
		self.salary = salary
		self.designation = designation
	
	def printDetails(self):
		return f'Name: {self.name}\nSalary: {self.salary}\nDesignation: {self.designation}\nNumber of leaves: {self.no_of_leaves}'
	
	def annualSalary(self):
		return int(self.salary)*12
	
	@classmethod
	def changeLeaves(cls, newleaves):
		cls.no_of_leaves = newleaves
	
	@staticmethod   # method which doesn't take self or cls as a parameter, just perform defined function
	def greet(string):
		return f'Hello! ' + string

class Player:
	no_of_sports = 4
	def __init__(self, name, sport):
		self.name = name
		self.sport = sport
	
	def printDetails(self):
		return f'Player: {self.name}\nSport: {self.sport}'

class CoolProgrammer(Employee, Player):
	languages = ['HTML', 'CSS', 'Python', 'JavaScript']

	def languageNeed(self):
		print(self.languages)

harry = Employee('Harry', 4500000, 'Senior Software Developer')
rohan = Employee('Rohan', 1500000, 'Junior Developer')

cr7 = Player('Cristiano', 'Football')

skillF = CoolProgrammer('SkillF', 500000, 'CoolProgrammer')

print(skillF.printDetails())
skillF.languageNeed()
print(skillF.no_of_leaves)
print(skillF.no_of_sports)

