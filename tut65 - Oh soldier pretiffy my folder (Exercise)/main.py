import os

# Creating new line remover function which will remove `\n` from list items
def removeNewLine(List):
	newList, List = List, []
	for string in newList:
		List.append(string.strip())
	return List


# reading ignore.txt and creating ignoreList out of it
with open('ignore.txt') as file:
	ignoreList = file.readlines()

# removing \n from each ignoreList item
ignoreList = removeNewLine(ignoreList)
print(ignoreList)

# Getting list of directory files
dirList = os.listdir()
print(dirList)

# Creating functions to do specific task
def lower():
	for x in dirList:
		if x not in ignoreList:
			os.rename(x, x.lower())

def upper():
	for x in dirList:
		if x not in ignoreList:
			os.rename(x, x.upper())

def regular():
	for x in dirList:
		if x not in ignoreList:
			os.rename(x, x.capitalize())

def jpgMagic():
	'''we will get those files which ends with `.jpg` & is not in ignoreList
	and then rename it to (number+default)'''
	renameInt = 1
	for i in dirList:
		if i.lower().endswith('.jpg') and i not in ignoreList:
			os.rename(i, f'{renameInt+1}{i}')
			renameInt += 1

def changeDir(dir):
	os.chdir(dir)
	print(os.getcwd())


if __name__ == "__main__":
	print('''\tWelcome to directory pretiffier\n\n1. Make files/folders in UPPERCASE\n2. Make files/folders in lowercase\n3. Make files/folders in Regular form\n4. Do some magic with .JPG files\n5. Change directory\n\n`q` to exit\n''')
	while True:
		choice = str(input('Choose: '))
		if choice == '1':
			upper()
		elif choice == '2':
			lower()
		elif choice == '3':
			regular()
		elif choice == '4':
			jpgMagic()
		elif choice == '5':
			inputDir = str(input('Change Dir: '))
			changeDir(inputDir)
		elif choice == 'q':
			quit()
		else:
			print('Choose between (1/2/3/4/q)')