import time
for i in range(0,2):
 print("--------")
 print("NCF")
 print("NCB")
 sel=str(input("Select the Type "))
 if(sel=="NCF"):
    print("Number Counting Forward")
    startnum=int(input("Enter the starting Number "))
    endnum=int(input("Enter the Ending Number "))
    timeon=float(input("Enter the Counting Speed(0.1 - 0.100) "))
    for i in range(startnum,endnum+1):
        time.sleep(timeon)
        print(i)
    print("Done!")
 elif(sel=="NCB"):
    print("Number Counting Backward")
    startnum1=int(input("Enter the starting Number "))
    endnum2=int(input("Enter the Ending Number "))
    timeon3=float(input("Enter the Counting Speed(0.1 - 0.100) "))
    for k in range(endnum2,startnum1-1):
        time.sleep(timeon3)
        print(k-startnum1)
    print("Done!")
 else:
    print("Invalid Input")