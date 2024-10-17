import datetime
import time
import os
while True:
    try:
        os.system("cls")
        print("Grade Certificate\n".upper())
        print("Enter your Firstname")
        Fname=input()
        print("Enter your Lastname")
        Lname=input()
        print("Enter your Age")
        age=input()
        print("Enter the your Exam Score")
        grade=int(input())
        if(grade<80):
            print(f"\nYour Score is {grade}.\nGet a Score above {grade} 👆 to get certified.")
        print("Which One do you Attend?\n(School/Colledge/University/Institude)")
        school=input()
        print("What did you Complete?")
        complete=input()
        print("Which Subject?")
        subject=input()
        print("")
        os.system("cls")
        if(grade>=100):
            time.sleep(2)
            print("\n------------------------------------")
            print("🎉Certificate of Excellence🎉\n".upper())
            print(f"This Certificate of Proudly Presented to {Fname} {Lname}")
            print(f"For Excelling in {complete} and {subject}")
            print(f"Attended {school}")
            print(f"Date : {datetime.date.today()}")
            print(f"Well Done {Fname} {Lname}!")
            print("\n------------------------------------")
        elif(grade>=90):
            time.sleep(2)
            os.system("cls")
            print("\n------------------------------------")
            print("🎉Certificate of Achievement🎉\n".upper())
            print(f"This Certificate of Proudly Presented to {Fname} {Lname}")
            print(f"For Doing Well in {complete} and {subject}")
            print(f"Attended {school}")
            print(f"Date : {datetime.date.today()}")
            print(f"Keep Going {Fname} {Lname}!")
            print("\n------------------------------------")
        else:
            print("Invalid Input".upper())
    except ValueError:
        os.system("cls")
        print("\nInvalid. Try Again.")
    exit()


