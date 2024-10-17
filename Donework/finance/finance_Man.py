import json
import os
import time
import sys
from tabulate import tabulate

def Home():
    try:
        def tools():
            print("\n=======TOOLS========")
            print("1 : Create Table")
            print("2 : Edit Table")
            print("3 : Delect Table")
            print("4 : Modify Tables")
            choicetools=int((input("> ")))
            if(choicetools==1):
                print("Enter table name")
                global tablename
                tablename=str(input("> "))
                print("Enter Table headers")
                global tableheader
                tableheader=str(input("> "))
                print("\nEnter Data")
                tabledata=str(input("| "))
                os.system("cls")
                def Table():
                    table_data = [[tabledata,tabledata]]

                    def calculate_column_widths(data):
                        column_widths = []
                        for col in range(len(data[0])):
                            column_width = max(len(str(row[col])) for row in data)
                            column_widths.append(column_width)
                        return column_widths

                    def print_table(data):
                        column_widths = calculate_column_widths(data)

                        for col, header in enumerate(data[0]):
                            print(f"{header:<{column_widths[col]}}", end=" | ")
                        print()
                        
                        for col_width in column_widths:
                            print("-" * col_width, end=" | ")
                        print()
                        
                        for row in data[1:]:
                            for col, value in enumerate(row):
                                print(f"{value:<{column_widths[col]}}", end=" | ")
                            print()

                    print_table(table_data)
                print("table created.")
                Table()
                globals()
                key=input("Press any key to continue")
                Home()
            elif(choicetools==2):
                pass
        os.system("cls")
        print("============HOME=================")
        print("you can now enter your data.\n\nTo create table press 1\nPress 3 for Calculator")
        # print("Your Table")
        # print(tabulate(Data,headers=tableheader,tablefmt="grid"))
        again=True
        while again:
            writer=str(input("|"))
            if(writer=='1'):
                os.system("cls")
                print("1 key is pressed.")
                time.sleep(2)
                os.system("cls")
                tools()
            elif(writer=='quit'.lower()):
                print("\nConfirm quit?")
                print("Yes or No")
                confirmquit=str(input("> ")).lower()
                if(confirmquit=="yes"):
                    os.system("cls")
                    print("Program terminated")
                    sys.exit()
                elif(confirmquit=="no"):
                    Home()
            elif(writer=='3'):
                os.system("cls")
                print("3 key was pressed")
                time.sleep(2)
                os.system("cls")
                try:
                    print("Calculator\n")
                    while True:
                        num=str(input(">"))
                        print(f"{eval(num)}")
                        if(num=='quit'):
                            Home()
                except Exception:
                    print("\nERROR : Invalid")
    except KeyboardInterrupt:
        os.system("cls")
        print("Program Interrupted.")
        sys.exit()    
    except Exception:
        os.system("cls")
        print("Ops! An error occured.")
        sys.exit()    
def Create():
    try:
        time.sleep(1)
        os.system("cls")
        print("Enter your new workspace")
        new_w=str(input("> "))
        workdata=open('workspacedata.txt','w')
        workdata.write(new_w)
        print("\nEnter name of your project")
        nameofproject=str(input("> "))
        workdata1=open('workspacedata.txt','w')
        workdata1.write(nameofproject)
        print("\nConfirm changes?")
        print("Yes or No")
        confirmchange=str(input("> ")).lower()
        if(confirmchange=="yes"):
            time.sleep(1)
            os.system("cls")
            print("creating your workspace...")
            time.sleep(3)
            os.system("cls")
            print("creating your project...")
            time.sleep(2)
            os.system("cls")
            time.sleep(2)
            print("Workspace was created")
            print(f"{nameofproject} was created.")
            enter=input("Press any key to continue")
            Home()
        elif(confirmchange=="no"):
            Create()
    except KeyboardInterrupt:
        os.system("cls")
        print("Program Interrupted.")
        sys.exit()    
    except Exception:
        # os.system("cls")
        print("Ops! An error occured.")
        sys.exit()    


def New():
    try:
        time.sleep(1)
        os.system("cls")
        print("Enter your new workspace")
        new_w=str(input("> "))
        workdata1=open('workspacedata.txt','w')
        workdata1.write(new_w)
        print("\nEnter name of your project")
        nameofproject=str(input("> "))
        workdata2=open('workspacedata.txt','w')
        workdata2.write(nameofproject)
        print("\nConfirm changes?")
        print("Yes or No")
        confirmchange=str(input("> ")).lower()
        if(confirmchange=="yes"):
            time.sleep(1)
            os.system("cls")
            print("creating your workspace...")
            time.sleep(3)
            os.system("cls")
            print("creating your project...")
            time.sleep(2)
            os.system("cls")
            time.sleep(2)
            print("Workspace was created")
            print(f"{nameofproject} was created.")
            enter=input("Press any key to continue")
            Home()
        elif(confirmchange=="no"):
            New()
    except KeyboardInterrupt:
        os.system("cls")
        print("Program Interrupted.")
        sys.exit()    
    except Exception:
        os.system("cls")
        print("Ops! An error occured.")
        sys.exit()    


def Man_workspace():
    os.system("cls")
    print("Your Workspaces are : ")
    workdata=open('workspacedata.txt','r')
    print(f"Project name : {workdata.read()}")

def Main():
    try:
        os.system("cls")
        print("="*23)
        print("Welcome To Personal Finance Manager")
        print("\nSelect from the Menu")
        print("1 : Create Workspace")
        print("2 : New Workspace")
        print("3 : Manage Workspaces")
        select=int(input("> "))
        if(select==1):
            Create()
        elif(select==2):
            New()
        elif(select==3):
            Man_workspace()
        else:
            print("\nInput required.")
    except KeyboardInterrupt:
        os.system("cls")
        print("Program Interrupted.")
        sys.exit()    
    except ValueError:
        os.system("cls")
        print("Ops! An error occured.")
        sys.exit()
Main()

            
