print("Hospital Appointment Schedule")
print("")
print("Please Select your Appointment")
print("1 : Morning Appointment")
print("2 : Everning Appointment")
print("3 : Afternoon Appointment")
choice=input("")
print("Enter your Hospital Name")
hospitalname=input("")
print("")
if(choice==("1")):
    print("\nMorning Appointment")
    print("Select your ⏲ Time of Appointment")
    print("1 : [6:30am-8:40am]")
    print("2 : [7:30am-9:30am]")
    print("3 : [5:30am-10:40am]")
    print("4 : [4:00am-8:30am]")
    choice1=input("")  
    if(choice1==("1")):
        print("\nYour Appointment is Schedule✅")
        print("Morning Appointment")
        print("6:30am-8:40am")
        print(f"We Will be Waiting for you at {hospitalname}")
    elif(choice1==("2")):
        print("\nYour Appointment is Schedule✅")
        print("Morning Appointment")
        print("7:30am-9:30am")
        print(f"We Will be Waiting for you at {hospitalname}")
    elif(choice1==("3")):
        print("\nYour Appointment is Schedule✅")
        print("Morning Appointment")
        print("5:30am-10:40am")
        print(f"We Will be Waiting for you at {hospitalname}")
    elif(choice1==("4")):
        print("\nYour Appointment is Schedule✅")
        print("Morning Appointment")
        print("4:00am-8:30am")
        print(f"We Will be Waiting for you at {hospitalname}")
    else:
        print("Pick A ⏲ Time for your Appointment")
elif(choice==("2")):
    print("\nEverning Appointment\n")
    print("Select your ⏲ Time of Appointment")
    print("1 : [5:00pm-7:30pm]")
    print("2 : [8:00pm-8:50pm]")
    print("3 : [6:20pm-8:30pm]")
    choice2=input("")
    if(choice2==("1")):
        print("\nYour Appointment is Schedule✅")
        print("Everning Appointment")
        print("5:00pm-7:30pm")
        print(f"We Will be Waiting for you at {hospitalname}")
    elif(choice2==("2")):
        print("\nYour Appointment is Schedule✅")
        print("Everning Appointment")
        print("8:00pm-8:50pm")
        print(f"We Will be Waiting for you at {hospitalname}")
    elif(choice2==("3")):
        print("\nYour Appointment is Schedule✅")
        print("Everning Appointment")
        print("6:20pm-8:30pm")
        print(f"We Will be Waiting for you at {hospitalname}")
    else:
        print("Pick A ⏲ Time for your Appointment")
elif(choice==("3")):
    print("Afternoon Appointment")
    print("Select your ⏲ Time of Appointment")
    print("1 : [11:00am-12:40pm]")
    print("2 : [12:00am-1:00pm]")
    print("3 : [2:30pm-5:40pm]")
    print("4 : [6:00pm-7:40pm]")
    choice3=input("")
    if(choice3==("1")):
        print("\nYour Appointment is Schedule✅")
        print("Afternoon Appointment")
        print("11:00am-12:40pm")
        print(f"We Will be Waiting for you at {hospitalname}")
    elif(choice3==("2")):
        print("\nYour Appointment is Schedule✅")
        print("Afternoon Appointment")
        print("12:00am-1:00pm")
        print(f"We Will be Waiting for you at {hospitalname}")
    elif(choice3==("3")):
        print("\nYour Appointment is Schedule✅")
        print("Afternoon Appointment")
        print("2:30pm-5:40pm")
        print(f"We Will be Waiting for you at {hospitalname}")
    elif(choice3==("4")):
        print("\nYour Appointment is Schedule✅")
        print("Afternoon Appointment")
        print("6:00pm-7:40pm")
        print(f"We Will be Waiting for you at {hospitalname}")
    else:
        print("Pick A ⏲ Time for your Appointment")
else:
    print("Please Select Appointment Hours ⌛")