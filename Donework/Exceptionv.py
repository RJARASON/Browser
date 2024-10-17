class JustnotcoolError(Exception):
    pass

x=2
try:
    raise JustnotcoolError("This just isn't cool,man")
except NameError:
    print("NameError means something is probably undefined")
except ZeroDivisionError:
    print("Do not divide by zero")
except Exception as error:
    print(error)
else:
    print('No Errors')
finally:
    print("I'm going to print with or without an Error")

