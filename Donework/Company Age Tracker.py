print("Company Age Tracker")
age=int(input("Enter your Age "))
gender=str(input("Enter your Gender (Male/Female) ")).lower()
if(age>22 and gender=="male"):
    print(f"{gender} Employee")
elif(age<=22 and gender=="male"):
    print(f"{gender} Intern!")
elif((age>22 and gender=="female")):
    print(f"{gender} Employee")
elif(age<=22 and gender=="female"):
    print(f"{gender} Intern!")
else:
    print("Please Enter your Age and Gender!")
