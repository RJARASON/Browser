def Calcu():
    try:
        print("Calculator\n")
        while True:
            num=str(input(">"))
            print(f"{eval(num)}")
    except Exception:
        print("\nERROR : Invalid")
Calcu()

