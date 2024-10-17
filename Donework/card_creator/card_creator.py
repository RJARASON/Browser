try:
    import os
    def Main():
        from utilities import Mastercard
        from utilities import VISA
        from utilities import virtual
        from utilities import B_Mastercard
        from utilities import B_VISA
        from utilities import B_Virtual
        os.system("cls")
        print("="*25)
        print("Welcome To MK virtual card💳 creator.")
        print("\nWho are you creating the card for?")
        print("1 : for Myself")
        print("2 : for Business")
        cht=int(input("> "))
        if(cht==1):
            for rerun2 in range(2):
                print("\nWhich type of card are you creating?")
                print("1 : Mastercard")
                print("2 : VISA")
                print("3 : virtual")
                cht1=int(input(""))
                if(cht1==1):
                    Mastercard()
                elif(cht1==2):
                    VISA()
                elif(cht1==3):
                    virtual()
                else:
                    print("\nInput required.")
                    continue
        elif(cht==2):
            for rerun3 in range(2):
                print("\nWhich type of card are you creating?")
                print("1 : Mastercard")
                print("2 : VISA")
                print("3 : virtual")
                cht1=int(input(""))
                if(cht1==1):
                    B_Mastercard()
                elif(cht1==2):
                    B_VISA()
                elif(cht1==3):
                    B_Virtual()
                else:
                    print("\n\nInput required.")
                    continue
    Main()
except Exception:
    os.system("cls")
    print("Oops! Something went wrong.")
    exit()

if __name__=="__main__":
    Main()