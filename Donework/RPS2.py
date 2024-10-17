import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3 

playagain=True

while playagain:
    print("1 : Rock")
    print("2 : Paper")
    print("3 : Scissors")
    choice=int(input(""))
    if choice<1|choice>3:
        sys.exit("You must choose 1,2,3")

    computerchoice=int(random.choice("123"))
    # computer=int(computerchoice)
    print("")
    print("You chose",str(RPS(choice)).replace('RPS.',''))
    print("Python chose",str(RPS(computerchoice)).replace('RPS.',''))
    print("")

    if(choice==1 and computerchoice==3):
        print("🎉You Win!")
    elif(choice==2 and computerchoice==1):
        print("🎉You Win!")
    elif(choice==3 and computerchoice==2):
        print("🎉You Win!")
    elif choice==computerchoice:
        print("⭕ Tie Game!")
    else:
        print("🐍Python Win!")

    playagain=input("\nPlay Again? \nY for Yes\nQ to Quit \n\n")
    if(playagain.lower()=="y"):
        continue
    else:
        print("Thank you for playing!\n")
        playagain=False 







