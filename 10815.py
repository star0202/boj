from re import A
from sys import stdin

input = stdin.readline


def bs(a, l):
    r = -1
    R = len(l)
    d = 0
    while R - r != 1:
        if int(l[(r + R) // 2]) > a:
            R = (r + R) // 2
            continue
        elif int(l[(r + R) // 2]) < a:
            r = (r + R) // 2
            continue
        else:
            d = 1
            break
    return d


input()
a = list(map(int, input().split()))
input()
b = list(map(int, input().split()))
c = []
a.sort()
for x in b:
    c.append(bs(x, a))
print(*c)
