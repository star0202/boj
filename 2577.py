a = int(input())
b = int(input())
c = int(input())
n = a * b * c
l = list(str(n))
l2 = []
for x in range(0, 10):
    l2.append(l.count(str(x)))
for x in l2:
    print(x)
