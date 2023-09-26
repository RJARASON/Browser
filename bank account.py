import time
x = 20
y = 1
print("------------------------------")
for i in range(0, 3):
    print("Your Bank Account is", x)
    ask = str(input("do you want to make a deposit? "))
    if (ask == ("Yes")):
        ask1 = int(input("How much? "))
        if ask1 < 80:
            print("You are about to put", ask1, "into your account.")
            time.sleep(1)
            prompt = str(input("Do you want to continue? "))
            if (prompt == ("Yes")):
                print("Loading....")
                time.sleep(4)
                x = ask1
                print("Complete! you money is now", x)
        if ask1 > 80:
            print("Hold on...")
            time.sleep(2)
            print("Please put money that is less than 80!")
        elif ask1 > x:
            print("Sorry, you only have small amount(", x, ")")
    else:
        print("Come back later.")
