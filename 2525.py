import datetime

h, m = map(int, input().split())
c = int(input())
n = datetime.timedelta(hours=h, minutes=m)
n += datetime.timedelta(minutes=c)
print(f"{int((n.seconds/60)//60)} {int(n.seconds/60-(n.seconds/60)//60*60)}")
