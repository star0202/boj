import datetime
a, b = map(int, input().split())
day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
print(day[datetime.datetime(2007, a, b).weekday()])