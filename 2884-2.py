import datetime
a,b=map(int,input().split(" "))
asdf=datetime.timedelta(hours=a,minutes=b)
qwer=asdf-datetime.timedelta(minutes=45)
print(f"{int((qwer.seconds/60)//60)} {int(qwer.seconds/60-(qwer.seconds/60)//60*60)}")