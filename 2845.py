l, p = map(int, input().split())
n = list(map(int, input().split()))
r = []
for x in range(5):
    r.append(n[x]-l*p)
print(*r, sep=" ")