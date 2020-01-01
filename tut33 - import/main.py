from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())

import sys
# Module finding heirarchy
print(sys.path)

import moduleFile as mdFile
print(mdFile.a)

mdFile.printjoke("This is me")
