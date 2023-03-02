n = int(input())
r = 0
for i in range(n):
    l = list(input().split("X"))
    for j in range(len(l)):
        c = l[j].count("O")
        while c != 0:
            r += c
            c -= 1
    print(r)
    r = 0
