import sys
import random
from enum import Enum
from enum import EnumType 
import os

playerscore=0
computerscore=0
gamecount=0
class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3
os.system("cls")
print("RPS Game")
name=str(input("Enter your Name to Play: "))
scorer=int(input("Enter Score reach: "))

while True:
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

    if(playerscore>=scorer):
            os.system("cls")
            print("================")
            print("Score Reach Ended.")
            print( name,"Score:",playerscore)
            print("Python Score:",computerscore)
            print("🏆🏆You Win!🏆🏆")
            print("================")
            exit()
    if(choice==1 and computerchoice==3):
        print("🎉You Win!")
        playerscore+=1
        print("Player Score:",playerscore,"\n")
    elif(choice==2 and computerchoice==1):
        print("🎉You Win!")
        playerscore+=1
        print("Player Score:",playerscore,"\n")
    elif(choice==3 and computerchoice==2):
        print("🎉You Win!")
        playerscore+=1
        print("Player Score:",playerscore,"\n")
    elif choice==computerchoice:
        print("⭕ Tie Game!")
    else:
        print("🐍Python Win!")
        computerscore+=1
        print("\nPython Score:",computerscore,"\n")
        if(computerscore==scorer):
            os.system("cls")
            print("================")
            print("Score Reach Ended.")
            print("Python Score",computerscore)
            print(name,"Score",playerscore)
            print("🏆🏆Python Win!🏆🏆")
            print("================")
            exit()
        continue
    gamecount+=1
