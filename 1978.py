import math

n = int(input())
i = list(map(int, input().split()))
r = 0


def prnum(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


for x in range(n):
    if i[x] != 1 and prnum(i[x]):
        r += 1
print(r)
