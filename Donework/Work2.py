print("Dictionary ")
band={
    "vocals":"Plants",
    "Music":"Piano"
}
band2=dict(vocals="Plants",Music="Piano") 

print(band)
print(band2)

#Access items
print(band["vocals"])
print(band.get("Music"))

#list all keys
print(band.keys())

#list all values
print(band.values())

#list of key/value pair as tuples
print(band.items())

#verify a key exists
print("Music"in band)
print("triangle"in band)

#Change values
band["vocals"]="kodjo"
band.update({"base":"JPE"})
print(band)

#Remove Items
print(band.pop("base"))
print(band)
band["Drums"]="Bonam"
print(band)
print(band.popitem())#tuple
print(band)

#Delect and Clear
band["Drums"]="Bonam"
del band["Drums"]
print(band)

band2.clear()
print(band2)

del band2


#Copy dictionaries

# band2=band #Create a reference
# print("Bad Copy!")
# print(band2)
# print(band)

# band2["Music"]="kodjo"
# print(band)

band2=band.copy()
band2["Music"]="kodjo"
print("Good Copy!")
print(band)
print(band2)

#or use the dict() constructor function

band3=dict(band) 
print("Good Copy!")
print(band3)


# Nested dictionaries

member1={
    "name":"Plant",
    "instrument":"vocals"
} 
member2={
    "name":"Page",
    "instrument":"validmeter"
} 
band={
    "member1":member1,
    "member2":member2
}
print(band)
print(band["member1"]["name"])



# from math import pi
# import sys
# import random as rdm
# from enum import Enum

# print(pi)
# for item in dir(rdm):
#     print(item)


