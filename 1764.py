from sys import stdin
input = stdin.readline
n, m = map(int, input().rstrip().split())
a = {}
b = []
r = 0
for _ in range(n):
    a[input().rstrip()] = 0
for _ in range(m):
    i = input().rstrip()
    try:
        if a[i] == 0:
            r += 1
            b.append(i)
    except:
        pass
print(r)
b.sort()
print(*b, sep="\n")