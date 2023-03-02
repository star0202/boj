from sys import stdin

a, b, v = map(int, stdin.readline().split())
k = (v - b) / (a - b)
if int(k) == k:
    print(int(k))
else:
    print(int(k) + 1)
