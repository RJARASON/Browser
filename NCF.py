import time
print("NCF")
print("NCB")
chose = str(input("Please select: "))
if (chose == ("NCF" or "ncf")):
    print("Number Counting Forward")
a = int(input("Enter the Starting number: "))
b = int(input("Enter the Ending number: "))
T = float(input("Enter the counting Speed(should be like[ 0.1 - 0.100]) "))
if a > 100:
    print("WOW! That's alot of Numbers")
    time.sleep(2)
elif b > 100:
    print("Thats alot!")
    time.sleep(2)
for i in range(a, b,):
    time.sleep(T)
    print(i)
if a == 100:
    print("The Number is alrady 100!")
else:
    print("Complete!")
if (chose == ("NCB" or "ncb")):
    print("Number Counting Backward")
a = int(input("Enter the starting number? "))
b = int(input("Enter the Ending number? "))
T = float(input("Enter the Count Speed "))
for i in range(b, a, -1):
    time.sleep(T)
    print(i)
else:
    print("Complete")
    print("Press 'F5' to Start Over")
