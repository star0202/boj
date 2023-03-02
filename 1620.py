from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
mondigit = {}
monname = {}
for x in range(n):
    i = input().rstrip()
    mondigit[x + 1] = i
    monname[i] = x + 1
for x in range(m):
    i = input().rstrip()
    if i.isdigit():
        print(mondigit[int(i)])
    else:
        print(monname[i])
