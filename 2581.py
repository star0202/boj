import math
def prnum(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True
m = int(input())
n = int(input())
r = []
for x in range(m, n+1):
    if x != 1 and prnum(x): r.append(x)
if len(r) == 0: print(-1)
else:
    r.sort()
    print(f"{sum(r)}\n{r[0]}")