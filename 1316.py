n = int(input())
r = 0
for x in range(n):
    i = input()
    l = list(i)
    for y in range(len(i)):
        if y + 1 != len(i):
            if i[y] == i[y+1]:
                l.remove(i[y])
    if len(l) == len(set(l)):
        r += 1
print(r)