#PALINDROME

string=input("Enter your name: ")
l=len(string)
rev=""
for i in range(l-1,-1,-1):
    rev+=string[i]
print(f"The reserved of {string.upper()} is {rev.upper()}")
if(rev.lower()==string.lower()):
    print(f"The {string.capitalize()} is a palindrome")
else:
    print(f"The {string.capitalize()} is not a palindrome")
