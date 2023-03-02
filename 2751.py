import sys

r = []
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    r.append(int(sys.stdin.readline().rstrip()))
r.sort()
for x in r:
    print(x)
