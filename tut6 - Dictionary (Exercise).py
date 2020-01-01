dictionary = {
    'set': 'Collection of well defined objects.',
    'name': 'Specific identity',
    "ignore": "Refuse to take notice of or acknowledge.",
    "abandon": "Cease to support or look after.",
    "exaggerate": "Enlarged or altered beyond normal proportions.",
    "prejudice": "Preconceived opinion that is not based on reason or actual experience."
}

word = str(input('Enter any word: '))

meaning = dictionary[word]

print('Meaning of', word, 'is', meaning)
