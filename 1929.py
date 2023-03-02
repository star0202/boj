import math


def prnum(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


m, n = map(int, input().split())
r = []
for x in range(m, n + 1):
    if x != 1 and prnum(x):
        r.append(x)
print(*r, sep="\n")
