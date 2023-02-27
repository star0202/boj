n = int(input())
i = []
for _ in range(n):
    a = input()
    if a not in i:
        i.append(a)
for x in range(51):
    b = []
    for y in i:
        if len(y) == x:
            b.append(y)
    if len(b) != 0:
        b.sort()
        print(*b, sep="\n")