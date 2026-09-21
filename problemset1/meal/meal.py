# efficient rewrite
def main():
    time = input("What time is it? ").strip().lower()
    mealtime = convert(time)

    if 7.0 <= mealtime <= 8.0:
        print("breakfast time")
    elif 12.0 <= mealtime <= 13.0:
        print("lunch time")
    elif 18.0 <= mealtime <= 19.0:
        print("dinner time")


def convert(time):
    # 12-hour format
    if "a.m." in time or "p.m." in time:
        clock, period = time.split()
        hour, minute = clock.split(":")

        hour = int(hour)
        minute = int(minute)

        if period == "a.m.":
            if hour == 12:
                hour = 0

        elif period == "p.m.":
            if hour != 12:
                hour += 12

    # 24-hour format
    else:
        hour, minute = time.split(":")
        hour = int(hour)
        minute = int(minute)

    return hour + minute / 60


if __name__ == "__main__":
    main()


# original version
""" def main():
    time = input("What time is it? ").lower()
    mealtime=convert(time)
    if mealtime != None:
        print(mealtime)

def convert(time=""):
    # 12 hour format
    if time.count("a.m.") == 1 or time.count("p.m.") == 1 :

        hour_minute = time.split()[0].split(":",2)
        hour = int(hour_minute[0])
        minute = int(hour_minute[1])

        if hour < 1 or hour > 12 or minute < 0 or minute > 59:
            return None

        # breakfast
        if time.count("a.m.") == 1 and ((hour == 7 and 0<=minute<=59) or (hour==8 and minute==0)):
            return "breakfast time"

        # luncha and dinner
        elif time.count("p.m."):
            if (hour==12 and 0<=minute<=59) or (hour==1 and minute==0):
                return "lunch time"
            elif (hour==6 and 0<=minute<=59) or (hour==7 and minute==0):
                return "dinner time"
    # 24 hour format
    else: 
        hour_minute = time.split(":",2)
        hour = int(hour_minute[0])
        minute = int(hour_minute[1])

        if hour < 0 or hour > 23 or minute < 0 or minute > 59:
            return None

        if (hour == 7 and 0 <= minute <= 59) or (hour == 8 and minute == 0):
            return "breakfast time"
        elif (hour == 12 and 0 <= minute <= 59) or (hour == 13 and minute == 0):
            return "lunch time"
        elif (hour == 18 and 0 <= minute <= 59) or (hour == 19 and minute == 0):
            return "dinner time"

if __name__ == "__main__":
    main()
 """
