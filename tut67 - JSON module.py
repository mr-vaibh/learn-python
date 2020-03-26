import json

# keys and values must be inside double quotes (mendatory)
data = '''{
    "key1": "value1",
    "key2": 45,
    "key3": true
}'''

# Converts stringified json object `data` to json dictionary `parsedData`
parsedData = json.loads(data)

# json.load(file) take file as a argument and runs a .read() function to that file argument
# and then convert it into dictionary `parsedData`
with open('data') as dataFile:
    parsedData = json.load(dataFile)

print(parsedData)
print(type(parsedData))

print(parsedData['key2'])
print(type(parsedData['key2']))



data2 = {
    'name': 'Vaibhav',
    'fav celebrities': ('Cristiano Ronaldo', 'Camila Cabelo', 'Robert Downey Jr.', 'Selena Gomez', 'Nawazuddin Siddiqui'),
    'car collection': ['Honada Amaze', 'Audi A4', 'BMW 760LI', 'Lamborghini Veneno Roadster', 'Bugatti Veron'],
    'profession': ['Developer Engineer', 'Bussiness Man', 'Footballer', 'Modal', 'Brand Ambassador', 'Influencer', 'Lover'],
    'age': 28,
    'humble': True
}

# json.dumps(data) takes python dictionary `data2` and returns JavaScript Compatible object `jscomp`
# after using this method, you can use returned object in JavaScript
jscomp = json.dumps(data2)
# sort_key attribute sorts the keys in alphabatically order
jscomp = json.dumps(data2, sort_keys=True)
jscomp = json.dumps(data2, sort_keys=False)
print(jscomp)

# notice that `True` key changes to `true` (lowercase)
# because it gets converted into JS compatible format
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

'''
Visit - https://www.w3schools.com/python/python_json.asp
to learn more
'''