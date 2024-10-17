import time
print("Number Guessing")
print("------------")
print("Select Your Difficulty")
print("Easy")
print("Medium")
print("Hard")
print("Extreme")
selection=str(input("Select your Difficulty "))
print("-----------")
print("RULES: You Will Be Given 3 Chances to Guess\nWhen it appears again that means you Guessed Wrong.\nIf you Guessed right it will Stop")
time.sleep(5)
if(selection==("Easy")):
   print("I'm thinking of a number from 1-10. What's the number? ")
   for i in range(0,3):
      guess1=str(input("Your Answer= "))
      if(guess1==("7")):
         print("Correct✅") 
         exit()
      else:
         print("Wrong Answer❌")
elif(selection==("Medium")):
   print("I'm thinking of a number from 2-11. What is the number?")
   for j in range(0,3):
      guess2=str(input("Your Answer= "))
      if(guess2==("10")):
         print("Correct✅")
         exit()
      else:
         print("Wrong Answer❌")
elif(selection==("Hard")):
   print("I'm thinking of a Number from 1-30. What is the number?")
   for k in range(0,3):
      guess3=str(input("Your Answer= "))
      if(guess3==("16")):
         print("Correct✅")
         exit()
      else:
         print("Wrong Answer❌")
elif(selection==("Extreme")):
   print("I'm thinking of a number from 5-35. What is the number?")
   for L in range(0,3):
      guess4=str(input("The number is start with 3\nYour Answer= "))
      if(guess4==("31")):
         print("Correct✅")
         exit()
      else:
         print("Wrong Answer❌")
else:
   print("Please Select your difficulty")