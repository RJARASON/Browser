# dicti={
#     "name":"",
#     "age":"",
#     "city":""
# }
# nam=input("Name: ")
# age=input("Age: ")
# city=input("City: ")
# dicti["name"]=nam
# dicti["age"]=age
# dicti["city"]=city
# print("")
# print(dicti)
# print("")

# delt=input("Delect? ")
# if(delt==("Yes")):
#     del dicti["name"]

names=["kodjo","Kofi","Daniel"]
actions=["eats","Codes","Play"]

# for name in names:
#     for action in actions:
#         print(name+" "+action+".")

for action in actions:
    for name in names:
        print(name+" "+action+".")