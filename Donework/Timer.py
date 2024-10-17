import time
import datetime
print("Set Timer ⏲")
hr=int(input("Enter Hours: "))
mins=int(input("Enter Minutes: "))
secs=int(input("Enter Seconds: "))

totalsecs=hr*3600+mins*60+secs

while totalsecs>0:
    timer=datetime.timedelta(seconds=totalsecs)
    print(timer ,end="\r")
    time.sleep(1)
    totalsecs-=1
else:
    print("Time Up!\n")
