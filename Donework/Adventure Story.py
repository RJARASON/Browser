from kmmodules.module import
"""An Adventure Game."""
try:
    print("Welcome To Adventure Game")
    name=input("Enter your Name to Play ")
    print("----------------")
    print("Hello",name,"Let' Begin!")
    print("--------------------")
    print("You are walking to go to the Mall and come\nacross a T road.")
    print("One way went left\nthe other way went right.\nWhich one will you take?")
    ans=input("(left/Right) ")
    if(ans==("Right")):
        print("--------------")
        print("You are walking 2km and you saw a Dog. Not knowing the dog will be dangerous or not\nWhat will you do?")
        ans1=input("(Pass around/play with it) ")
        if(ans1==("Pass around")):
            print("----------\nYou passed near the dog and you went to the Mall")
            print("you are in the Mall")
            print("And you buy your stuff and went to pay for them. But you don't have enought money.")
            print("What you going to do?")
            ans3=input("(Get money from an ATM/Just leave) ")
            if(ans3==("Get money from an ATM")):
                print("---------\nyou quickly go and take money from an ATM and pay for them.")
                print("you left with your stuffs in your hands")
                print("You Won!")
            elif(ans3==("Just leave")):
                print("You left without nothing in your hand")
                print("You Lose! Game Over")
        elif(ans1==("play with it")):
            print("----------\nyou were playing with the dog and the dog bite you")
            print("What will you do?")
            ans2=input("(Go to the Hospital/Report) ")
            if(ans2==("Go to the Hospital")):
                print("Good Choice! You Win!")
            elif(ans2==("Report")):
                print("---------\nYou reported that you got bitten by the dog.")
                print("Before you left you fell down to the Ground")
                print("Bad Choice!You Lose.Game Over!")
        else:
            print("No Choice.Game Over")
    elif(ans=="left"):
        print("-------------------")
        print("you decided to take the left.\nWhen Gangters attack you and took you money")
        print("And they ran away with a car")
        print("Will you call the cops or chase after them?")
        ans4=input("(Call the Cops/Chase them) ")
        if(ans4==("Call the Cops")):
            print("----------------\nYou took your phone and you dial 911.")
            print("The Cops responded and chase after them.")
            print("In 1hr time, they returned and arrested the Gangters")
            print("and you have your money back")
            print("You Won!")
        elif(ans4==("Chase them")):
            print("------------\nyou took a car and you went after them")
            print("but a Tanker came in the way,what will you do?")
            ans5=input("(Try and Pass/Stop) ")
            if(ans5==("Try and Pass")):
                print("-----------\nyou were speeding and passed right in front of it")
                print("But the Tanker came to close and hit you")
                print("You Died! Game Over")
            elif(ans5==("Stop")):
                print("----------------\nyou stop and let the Tanker pass before you go")
                print("But the Gangters got away")
                print("You Lose! Game Over")
            else:
                print("No Choice.Game Over")
    else:
        print("Invalid.Game Over")
except ValueError:
    print("Invalid. try again.")
    exit()