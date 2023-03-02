import sys

n = int(sys.stdin.readline().rstrip())
c = [0] * 10001
for _ in range(n):
    i = int(sys.stdin.readline().rstrip())
    c[i] += 1
for i in range(1, 10001):
    if c[i] != 0:
        for _ in range(c[i]):
            print(i)
