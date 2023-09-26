import time
a = str(input("Choose one: str or int: "))
if (a == ("str")):
    a = str(input("What is your name? "))
    for b in range(0, -1):
        chr = a
        print(a)
elif (a == ("int")):
    a = int(input("Enter your age: "))
    for i in range(0, a):
        print(i-a)
else:
    print("Please say str or int")
