try:
    import time
    import random
    chara="abcdefjhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*/12345678910"
    print("Password Generator\n")
    num=int(input("Enter Password Lenght: "))
    print("\n")
    for j in range(0,num):
        print(random.choice(chara),end="")
    print("\n⚠ Copy this password somewhere safe")
except Exception:
    print("System error.")
    exit()