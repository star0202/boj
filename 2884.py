import datetime

h, m = map(int, input().split())
n = datetime.timedelta(hours=h, minutes=m)
n -= datetime.timedelta(minutes=45)
print(f"{int((n.seconds/60)//60)} {int(n.seconds/60-(n.seconds/60)//60*60)}")
