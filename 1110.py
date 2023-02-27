fir=int(input())
new=0
cycle=0
while new!=fir:
    if cycle==0:
        sec=(fir%10)+(fir//10)
        new=(10*(fir%10))+(sec%10)
        cycle+=1
    elif cycle>=1:
        sec=(new%10)+(new//10)
        new=(10*(new%10))+(sec%10)
        cycle+=1
if fir==0:
    cycle=1
print(cycle)