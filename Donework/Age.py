import datetime
import time
try:
    y=int(input("Your Year: "))
    cy=int(input("Current Year: "))
    if(y>cy):
        print("--------")
        print("You can't Be Born in the Future🤚\n" "")
    elif(y>=2025):
        print("Hello People from the Future👋")
    else:
        print("\nyou are",cy-y,"years old")
except Exception:
    print("\nERROR : Invalid Input.")