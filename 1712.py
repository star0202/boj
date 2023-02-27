from sys import stdin
a, b, c = map(int, stdin.readline().split())
if c-b == 0: print(-1)
else:
    n = a/(c-b)+1
    if n <= 0: print(-1)
    else: print(int(n))