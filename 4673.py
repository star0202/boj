m = []
for i in range(1, 10000):
    k = list(str(i))
    for j in k:
        i += int(j)
    m.append(i)
for p in range(1, 10000):
    if p not in m:
        print(p)
