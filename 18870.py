from sys import stdin
input = stdin.readline
n = int(input())
l = list(map(int, input().split()))
a = sorted(list(set(l)))
r = {a[i] : i for i in range(len(a))}
for i in l:
    print(r[i], end = ' ')