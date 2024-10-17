def TimeBased():
    from datetime import datetime
    current_time = datetime.now()
    if current_time.hour < 12:
        print("Good morning!")
    elif 12 <= current_time.hour < 18:
        print("Good afternoon!")
    else:
        print("Good evening!")
TimeBased()


















