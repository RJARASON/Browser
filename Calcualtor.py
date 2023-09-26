import time
print("Calculator")
for i in range(0,4):
 print("What number you want to write")
 num1=int(input("Enter the first number: "))
 num2=int(input("Enter the Second number: "))
 num3=int(input("Enter the third number: "))
 num4=int(input("Enter the fourth number: "))
 print("Write the operator you want to use: ")
 operator=str(input("What is the operator: "))
 if(operator=="+"):
     print(num1+num2+num3+num4)
 elif(operator=="-"):
     print(num1-num2-num3-num4)
 elif(operator=="*"):
     print(num1*num2*num3*num4)
 elif(operator=="/"):
     print(num1/num2/num3/num4)
 elif(operator=="%"):
     print(num1%num2%num3%num4)
 else:
    print("Where's Operator?❌❓")