n = int(input())
i = []
for x in range(1,n):
    a = x
    for y in range(len(str(x))):
        a += int(str(x)[y])
    if a == n: i.append(x)
try: print(min(i))
except: print(0)