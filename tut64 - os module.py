import os

# Methods, attributes which we can use in OS modules
# print(dir(os))

# Current working directory
print(os.getcwd())

# Change working directory
os.chdir('D:/Vaibhav/Images')
print(os.getcwd())
os.chdir('D:/Vaibhav/Python/lessons')

# List of all files and folders in current or passed dir
print(os.listdir('C:'))


# Create a folder
# Folder will be created in current or changed dir
# will throw error if already exists
os.mkdir('Folder created by os module `tut64`') if not os.path.exists('Folder created by os module `tut64`') else print('folder already exists')

# Careful its `makedirs` not `mkdir`
os.makedirs('folder/sub-folder') if not os.path.exists('folder') else print('folders already exists')

# Renaming file or folder
os.rename('folder', 'Folder')

# Read environment variable
print(os.environ.get('Path'))

# Join two paths (remove extra slashes, if exists, must use when joining paths)
print(os.path.join('C://', '/Windows'))

# Check if path exists
print(os.path.exists('C://Windows'))

# Check if path exists
print(os.path.isdir('C://koi bhi folder'))

''' Difference between `os.path.exists` and `os.path.isdir`
`os.path.exists` will also return True if there's a regular file with that name.
`os.path.isdir` will only return True if that path exists and is a directory, or a symbolic link to a directory.

Source - https://stackoverflow.com/questions/15077424/pros-and-cons-between-os-path-exists-vs-os-path-isdir
'''

# Check if it is a file
print(os.path.isfile('C://Windows'))
