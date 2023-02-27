n = input()
l = []
for x in range(len(n)):
    l.append(int(n[x]))
l.sort(reverse=True)
print(*l, sep="")