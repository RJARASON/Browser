try:
    import time
    import sys
    import os
    def Mastercard():
        os.system("cls")
        print("="*20)
        print("MASTERCARD\n")
        print("Please wait...")
        time.sleep(3)
        rerun1=True
        while rerun1:
            try:
                print("="*22)
                print("Enter cardHolder Name")
                cardname=str(input(""))
                print("\nEnter card number")
                cardnum=int(input(""))
                print("\nEnter the expiry date")
                cardexpiry=str(input(""))
                if(cardexpiry.__contains__("/")):
                    print("\nEnter card CVV")
                    cardcvv=int(input(""))
                    print("\nEnter the name of the bank that issued the card.")
                    bank=str(input(""))
                    print("\nSign your card")
                    signature=str(input(""))
                    print("="*22)
                    print("\ncreating your card.....")
                    time.sleep(4)
                    os.system("cls")
                    print("="*20)
                    print("🎉Your Card was created!🎉".upper())
                    print("")
                    print("-----------------------------------------------------")
                    print(f"| BANK LOGO : {bank}                                ")
                    print(f"|                                                   ")
                    print(f"| {cardname}                                        ")
                    print(f"|                            MASTERCARD             ")
                    print(f"| {cardnum}                                         ")                        
                    print(f"| Expiry Date : {cardexpiry}    CVV : {cardcvv}     ")
                    print("-----------------------------------------------------")
                    print("")
                    sys.exit()
                else:
                    print("\nInvalid Expiry Date.\nTry again")
                    time.sleep(2)
                    os.system("cls")
                    rerun1
            except Exception:
                print("Input is required!")
                time.sleep(1)
                os.system("cls")
                rerun1    

    def VISA():
        os.system("cls")
        print("="*20)
        print("VISA\n")
        print("Please wait...")
        time.sleep(3)
        rerun2=True
        while rerun2:
            try:
                print("="*22)
                print("Enter cardHolder Name")
                cardname=str(input(""))
                print("\nEnter card number")
                cardnum=int(input(""))
                print("\nEnter the expiry date")
                cardexpiry=str(input(""))
                if(cardexpiry.__contains__("/")):
                    print("\nEnter card CVV")
                    cardcvv=int(input(""))
                    print("\nEnter the name of the bank that issued the card.")
                    issingbank=str(input(""))
                    print("\nSign your card")
                    signature=str(input(""))
                    print("="*22)
                    print("\ncreating your card.....")
                    time.sleep(4)
                    os.system("cls")
                    print("="*20)
                    print("🎉Your Card was created!🎉".upper())
                    print("")
                    print("---------------------------------------------------")
                    print(f"| BANK LOGO : {issingbank}                        ")
                    print(f"|                                                 ")
                    print(f"| {cardname}                                      ")
                    print(f"|                         VISA CARD               ")
                    print(f"| {cardnum}                                       ")                        
                    print(f"| Expiry Date : {cardexpiry}    CVV : {cardcvv}   ")
                    print("---------------------------------------------------")
                    print("")
                    sys.exit()
                else:
                    print("\nInvalid ExpiryDate.\nTry again")
                    time.sleep(2)
                    os.system("cls")
                    rerun2
            except Exception:
                print("Input is required!")
                time.sleep(1)
                os.system("cls")
                rerun2

    def virtual():
        os.system("cls")
        print("="*20)
        print("VIRTUAL\n")
        print("Please wait...")
        time.sleep(3)
        rerun3=True
        while rerun3:
            try:
                print("="*22)
                print("Enter cardHolder Name")
                cardname=str(input(""))
                print("\nEnter card number")
                cardnum=int(input(""))
                print("\nEnter the expiry date")
                cardexpiry=str(input(""))
                if(cardexpiry.__contains__("/")):
                    print("\nEnter card CVV")
                    cardcvv=int(input(""))
                    print("\nEnter card type")
                    issingbank=str(input(""))
                    print("\nSign your card")
                    signature=str(input(""))
                    print("="*22)
                    print("\ncreating your card.....")
                    time.sleep(4)
                    os.system("cls")
                    print("="*20)
                    print("🎉Your Card was created!🎉".upper())
                    print("\n-------------------------------------------------")
                    print(f"| BANK LOGO : {issingbank}                        ")
                    print(f"|                                                 ")
                    print(f"| {cardname}                                      ")
                    print(f"|                        VIRTUAL CARD             ")
                    print(f"| {cardnum}                                       ")                        
                    print(f"| Expiry Date : {cardexpiry}    CVV : {cardcvv}   ")
                    print("-------------------------------------------------\n")
                    sys.exit()
                else:
                    print("\nInvalid ExpiryDate\nTry again")
                    time.sleep(2)
                    os.system("cls")
                    rerun3
            except Exception:
                print("Input is required!")
                time.sleep(1)
                os.system("cls")
                rerun3

    def B_Mastercard():
        os.system("cls")
        print("="*20)
        print("BUSINESS MASTERCARD\n")
        print("Please wait...")
        time.sleep(3)
        rerun1=True
        while rerun1:
            try:
                print("="*22)
                print("Enter cardHolder Name")
                cardname=str(input(""))
                print("\nEnter card number")
                cardnum=int(input(""))
                print("\nEnter the expiry date")
                cardexpiry=str(input(""))
                if(cardexpiry.__contains__("/")):
                    print("\nEnter card CVV")
                    cardcvv=int(input(""))
                    print("\nEnter the name of the bank that issued the card.")
                    bank=str(input(""))
                    print("Enter Business name")
                    businessname=str(input(""))
                    print("\nSign your card")
                    signature=str(input(""))
                    print("="*22)
                    print("\ncreating your card.....")
                    time.sleep(4)
                    os.system("cls")
                    print("="*20)
                    print("🎉Your Card was created!🎉".upper())
                    print("")
                    print("-----------------------------------------------------")
                    print(f"| BANK LOGO : {bank}                                ")
                    print(f"|                                                   ")
                    print(f"| {cardname}               BUSINESS MASTERCARD      ")
                    print(f"|                                                   ")
                    print(f"|                   Business Name : {businessname}  ")
                    print(f"| {cardnum}                                         ")                        
                    print(f"| Expiry Date : {cardexpiry}    CVV : {cardcvv}     ")
                    print("-----------------------------------------------------")
                    print("")
                    sys.exit()
                else:
                    print("\nInvalid ExpiryDate.\nTry again.")
                    time.sleep(2)
                    os.system("cls")
                    rerun1
            except Exception:
                print("Input is required!")
                time.sleep(1)
                os.system("cls")
                rerun1 
    def B_VISA():
        os.system("cls")
        print("="*20)
        print("BUSINESS VISA CARD\n")
        print("Please wait...")
        time.sleep(3)
        rerun2=True
        while rerun2:
            try:
                print("="*22)
                print("Enter cardHolder Name")
                cardname=str(input(""))
                print("\nEnter card number")
                cardnum=int(input(""))
                print("\nEnter the expiry date")
                cardexpiry=str(input(""))
                if(cardexpiry.__contains__("/")):
                    print("\nEnter card CVV")
                    cardcvv=int(input(""))
                    print("\nEnter the name of the bank that issued the card.")
                    bank=str(input(""))
                    print("Enter Business name")
                    businessname=str(input(""))
                    print("\nSign your card")
                    signature=str(input(""))
                    print("="*22)
                    print("\ncreating your card.....")
                    time.sleep(4)
                    os.system("cls")
                    print("="*20)
                    print("🎉Your Card was created!🎉".upper())
                    print("")
                    print("-----------------------------------------------------")
                    print(f"| BANK LOGO : {bank}                                ")
                    print(f"|                                                   ")
                    print(f"| {cardname}               BUSINESS VISA CARD       ")
                    print(f"|                                                   ")
                    print(f"|                   Business Name : {businessname}  ")
                    print(f"| {cardnum}                                         ")                        
                    print(f"| Expiry Date : {cardexpiry}    CVV : {cardcvv}     ")
                    print("-----------------------------------------------------")
                    print("")
                    sys.exit()
                else:
                    print("\nInvalid ExpiryDate.\nTry again")
                    time.sleep(2)
                    os.system("cls")
                    rerun2
            except Exception:
                print("Input is required!")
                time.sleep(1)
                os.system("cls")
                rerun2    
    def B_Virtual():
        os.system("cls")
        print("="*20)
        print("BUSINESS VIRTUAL CARD\n")
        print("Please wait...")
        time.sleep(3)
        rerun3=True
        while rerun3:
            try:
                print("="*22)
                print("Enter cardHolder Name")
                cardname=str(input(""))
                print("\nEnter card number")
                cardnum=int(input(""))
                print("\nEnter the expiry date")
                cardexpiry=str(input(""))
                if(cardexpiry.__contains__("/")):
                    print("\nEnter card CVV")
                    cardcvv=int(input(""))
                    print("\nEnter the name of the bank that issued the card.")
                    bank=str(input(""))
                    print("Enter Business name")
                    businessname=str(input(""))
                    print("\nSign your card")
                    signature=str(input(""))
                    print("="*22)
                    print("\ncreating your card.....")
                    time.sleep(4)
                    os.system("cls")
                    print("="*20)
                    print("🎉Your Card was created!🎉".upper())
                    print("")
                    print("-----------------------------------------------------")
                    print(f"| BANK LOGO : {bank}                                ")
                    print(f"|                                                   ")
                    print(f"| {cardname}               BUSINESS VIRTUAL CARD    ")
                    print(f"|                                                   ")
                    print(f"|                   Business Name : {businessname}  ")
                    print(f"| {cardnum}                                         ")                        
                    print(f"| Expiry Date : {cardexpiry}    CVV : {cardcvv}     ")
                    print("-----------------------------------------------------")
                    print("")
                    sys.exit()
                else:
                    print("\nInvalid ExpiryDate.\nTry again.")
                    time.sleep(2)
                    os.system("cls")
                    rerun3
            except Exception:
                print("Input is required!")
                time.sleep(1)
                os.system("cls")
                rerun3
    # class Expirydate:
    #     print(f"{random.choice(string.digits)}{random.choice(string.digits)}/{random.choice(string.digits)}/{datetime.datetime.now().year}")

    # class Cardnum:
    #     print(''.join([str(random.randint(0,5)) for _ in range(16)]))

except Exception:
    os.system("cls")
    print("Error with the utilities file.")
    exit()

