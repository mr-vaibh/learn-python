# Dictionary is nothing but key value pairs
d1 = {}
# print(type(d1))
d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
# d2["Ankit"] = "Junk Food"
# d2[420] = "Kebabs"
# print(d2)
# del d2[420]
# print(d2["Shubham"])

# below code will not create a new d3
# if u remove something from d3, it will also be removed from d2
d3 = d2

# now this code will create new d3 as a copy of d2
d3 = d2.copy()

del d3["Harry"]

print(d2.get('Harry'))
d2.update({"Leena":"Toffee"})
print(d2.keys())
print(d2.items())
