from functools import cmp_to_key
k, n = map(int, input().split())
a = []
for _ in range(k):
    a.append(int(input()))
m = max(a)
for _ in range(n-len(a)):
    a.append(m)
a = sorted(a, key=cmp_to_key(lambda c, d: -1 if int(str(c) + str(d)) > int(str(d) + str(c)) else 1))
print(*a, sep="")