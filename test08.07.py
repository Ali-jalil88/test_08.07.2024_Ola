#Example of dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#Note year only appear in one time because it is key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
#From Python's perspective, dictionaries are defined as objects with the data type 'dict':
print(type(thisdict))
capital_city = {
    "Nepal": "Kathmandu",
    "Italy": "Rome",
    "England": "London"
}
print(capital_city)
print(capital_city.keys())
print(capital_city.values())
print(capital_city["England"])

print("Initial Dictionary: ",capital_city)
capital_city["Japan"] = "Tokyo"
print("Updated Dictionary: ",capital_city)

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)
student_id[112] = "Stan"
print("Updated Dictionary: ", student_id)

print("Before remove from Dictionary: ", student_id)
del student_id[111]
print("After remove from Dictionary: ", student_id)
#del student_id
print(student_id) #this will cause an error because "thisdict" no longer exists.

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
#Print all key names in the dictionary, one by one-
for i in student_id:
    print(i)

#Print all values in the dictionary, one by one-
for x in student_id:
    print("Kyle" in student_id[x] , x)

new_dict = {}
student_id2 = {114: "Eric", 115: "Kyle", 116: "Butters"}
new_dict = student_id2
print(new_dict)

student_id2.clear()
print(new_dict)
new_dict1 = {}
student_id2 = {114: "Eric", 115: "Kyle", 116: "Butters"}
new_dict1 = student_id2.copy()
print(new_dict1)

student_id2.clear()
print(new_dict1)

#Create a dictionary that contain three dictionaries-
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
#Create three dictionaries, then create one dictionary that will contain the other three dictionaries-
child4 = {
  "name" : "Emil",
  "year" : 2004
}
child5 = {
  "name" : "Tobias",
  "year" : 2007
}
child6 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily1 = {
  "child4" : child4,
  "child5" : child5,
  "child6" : child6
}
print(myfamily1)    
print(myfamily["child2"]["name"])

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print(len(student_id))
