from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
a = {}
r = 0
for _ in range(n):
    i = input()
    a[i] = True
for _ in range(m):
    i = input()
    if i in a.keys():
        r += 1
print(r)