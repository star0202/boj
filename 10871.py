n, x = map(int, input().split())
a = input().split()
r = []
for i in range(0, n):
    if int(a[i]) < x:
        r.append(a[i])
print(" ".join(map(str, r)))