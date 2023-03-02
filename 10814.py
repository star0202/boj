from sys import stdin

n = int(stdin.readline())
i = []
for _ in range(n):
    a, b = stdin.readline().split()
    i.append((int(a), b))
i.sort(key=lambda x: x[0])
for x in i:
    print(x[0], x[1])
