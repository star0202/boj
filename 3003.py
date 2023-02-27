a, b, c, d, e, f = map(int, input().split())
r = []
r.append(1-a)
r.append(1-b)
r.append(2-c)
r.append(2-d)
r.append(2-e)
r.append(8-f)
print(*r, sep=" ")