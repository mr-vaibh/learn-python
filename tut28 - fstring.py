# F strings

''' Old practise, might be confusing 
if too many number of %s are present in current module

name = 'harry'
a = 'this is %s'%name
print(a)
'''
# greet = 'Hello!'
# name = 'Anubhav'
# txt = '%s my name is %s.'%(greet, name)
# print(txt)

########################################################################

''' Another a bit old practise
greet, name = 'Hello!', 'Anubhav'
txt = '{} my name is {}.'
txt = txt.format(greet, name)
print(txt)
'''

# txt = '{2} my name is {0} and I am a successful {1}.'
# txt = txt.format('Anubhav', 'actor', 'Hi,')
# print(txt)

########################################################################

# F string concept  (f means `fast`)
greet, name, profession = 'Hi,', 'Anubhav', 'actor'
txt = f'{greet} my name is {name} and I am a successful {profession}.'
print(txt)
