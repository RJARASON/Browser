import holder
import sys

def login(user="user",passw=0000):
    users=holder.users_list.keys()
    passc=holder.users_list.values()
    while True:
        try:
            print("=======================")
            print("Login".upper())
            userinput=str(input("Enter your username: "))
            passinput=int(input("Enter your password: "))

            if(userinput in users or userinput==user):
                if(passinput in passc or passinput==passw):
                    print(f"👋 Hello {userinput}!")
                else:
                    print("\nInvalid Password.")
            else:
                print("\nUsername not found.\n")
        except Exception:
            print("\nTransaction Failed.")
        sys.exit()


login(user="user",passw=0000)



