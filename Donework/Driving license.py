import time
import sys
import random
numbers="325","456","489","968","456","956","235"
print("Driving License🚘")
print("A : Car license")
print("B : Moto license")
select=str(input("")).upper()
if(select==("A")):
    print("Car license")
    print("")
    print("Please Fill the form")
    name=str(input("Name: "))
    age=int(input("Age: "))
    if(age<18):
        print("\nSorry, you are not of age.\n")
        exit()
    gender=str(input("Gender: ")).upper()
    city=str(input("City: "))
    number=str(input("Mobile Number(should include country code): "))
    if (number.__contains__("+")):
        print("\nPlease wait...\n")
        time.sleep(7)
        print("==================")
        print("Driving license")
        print(f"Name {name}")
        print(f"Age {age}")
        print(f"Gender {gender}")
        print(f"City {city}")
        print(f"Mobile number {number}")
        drivinglicenseNo=int(random.choice(numbers))
        print(f"Driving license Number : 465956426: {drivinglicenseNo}")
        print("==================\n")
    else:
        print("\nInvalid mobile number(forgot postal code)\n")
        exit()
elif(select==("B")):
    print("Moto license")
    print("\nPlease Fill the form")
    name1=str(input("Name: "))
    age1=int(input("Age: "))
    if(age1<18):
        print("\nSorry, you are not of age.\n")
        exit()
    gender1=str(input("Gender: ")).upper()
    city1=str(input("City: "))
    number1=str(input("Mobile Number(should include country code): "))
    if (number1.__contains__("+")):
        print("\nPlease wait...\n")
        time.sleep(7)
        print("==================")
        print("Driving license")
        print(f"Name {name1}")
        print(f"Age {age1}")
        print(f"Gender {gender1}")
        print(f"City {city1}")
        print(f"Mobile number {number1}")
        drivinglicenseNo1=int(random.choice(numbers))
        print(f"Driving license Number : 478462: {drivinglicenseNo1}")
        print("==================\n")
    else:
        print("\nInvalid mobile number(forgot postal code)\n")
        exit()
else:
    print("\nInvalid!\n")