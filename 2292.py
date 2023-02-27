from sys import stdin
n = int(stdin.readline())
a = 1
c = 1
if n == 1: print(1)
else:
    while n > a:
        a += (6*c)
        c += 1
    print(c)