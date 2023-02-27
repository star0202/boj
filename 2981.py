import math
from sys import stdin
input = stdin.readline
t = int(input())
s = []
a = []
g = 0
for i in range(t):
    s.append(int(input()))
    if i == 1:
        g = abs(s[1]-s[0])
    g = math.gcd(abs(s[i]-s[i - 1]), g)
ga = int(g**0.5)
for i in range(2, ga+1):
    if g % i == 0:
        a.append(i)
        a.append(g//i)
a.append(g)
a = list(set(a))
a.sort()
print(*a)