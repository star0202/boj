def bs(a, l):
    r = -1
    R = len(l)
    d = 0
    while R - r != 1:
        if int(l[(r + R) // 2]) > a:
            R = (r + R) // 2
            continue
        elif int(l[(r + R) // 2]) < a:
            r = (r + R) // 2
            continue
        else:
            d = 1
            break
    return d


x1 = input()
l = list(map(int, input().split()))
x2 = input()
n = list(input().split())
l.sort()
for i in n:
    print(bs(int(i), l))
