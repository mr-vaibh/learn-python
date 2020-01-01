'''Args and Kwargs are always optional'''

''' In normal functions there would be problem if we add more than expected params '''
# def funcNamePrint(a, b, c, d, e):
# 	print(a, b, c, d, e)
# funcNamePrint('Harry', 'Rohan', 'SkillF', 'Shivam', 'Anubhav')



''' Syntax:          function(normalParam, *args, **kwargs)    
--> We can pass as many parameters as we want and it will be stored as a tuple in *args
	and as a dictionary in **kwargs
--> It is not important to name it *args/**kwargs, it can be anything like *anubhav ;)
--> It is vital requirement to pass *args after any other normal parameter
	and to pass **kwargs after *args otherwise it will throw error
'''


def funArgs(normal, *args, **kwargs):
	print('Type of *args', type(args))
	print(normal)
	for item in args:
		print(item)

	print('Type of **kwargs', type(kwargs))
	print("\nNow I would Like to introduce some of our heroes")
	for key, value in kwargs.items():
		print(f"{key} is a {value}")


normal = "I am a normal Argument and the students are:"
names = ["Harry", "Rohan", "Skillf", "Hammad", "Shivam", "The programmer"]
staff = {"Rohan": "Monitor",
		 "Harry": "Fitness Instructor",
		 "The Programmer": "Coordinator",
		 "Shivam": "Cook"}

funArgs(normal, *names, **staff)
