import sys
import warnings
import os
class Systemfailure(Exception):
    pass

# def symb(symbol:sys.int_info)->None:...

# warnings.warn(category=Warning,source=1,message="Hello,this is urgent!",stacklevel=1)
os.system("cls")
print(warnings.showwarning(category=Warning,filename="Game.py",message="This File is unsuported!",lineno=6))