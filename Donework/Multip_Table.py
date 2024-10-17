import time
print("Multiplication Table\n---------")
a=int(input("Enter the first Number "))
b=int(input("Enter the Number of times it will Mutiply "))
timeout=str(input("\nDo you want it one by one\nor just put it on the screen (Y/N)\n "))
if(timeout=="Y"): 
    print("-----")
    T=float(input("Enter the Counting Speed (1 - 0.100) ")) 
    print(a,"Multiplication Table (by",b,"times)")
    for i in range(1,b+1):
        time.sleep(T)
        print(a,"*",i,"=",a*i)
elif(timeout=="N"):
    print("-----")
    print(a,"Multiplication Table (by",b,"times)")
    for i in range(1,b+1):
        print(a,"*",i,"=",a*i)
else:
    print("Make your Sugguest (Y/N)")

