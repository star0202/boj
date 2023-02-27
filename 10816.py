from sys import stdin
input = stdin.readline
input()
dict = {}
i = input().rstrip().split()
for x in i:
    try:
        dict[x] += 1
    except:
        dict[x] = 1
input()
i = input().rstrip().split()
r = []
for x in i:
    try:
        r.append(dict[x])
    except:
        r.append(0)
print(*r)