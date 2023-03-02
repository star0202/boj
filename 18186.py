from sys import stdin

input = stdin.readline

n, b, c = map(int, input().split())
if b < c:
    c = b
l = list(map(int, input().split()))
ans = 0

for x in range(n - 2):
    if l[x + 1] > l[x + 2]:  # 2개
        best = min(l[x], l[x + 1] - l[x + 2])
        ans += best * (b + c)
        l[x] -= best
        l[x + 1] -= best
    if l[x] > 0:  # 3개
        if l[x + 1] > 0 and l[x + 2] > 0:
            best = min(l[x], l[x + 1])
            ans += best * (b + c + c)
            l[x] -= best
            l[x + 1] -= best
            l[x + 2] -= best
            ans += l[x] * b
        else:  # 1개
            ans += l[x] * b
if l[-2] > 0 and l[-1] > 0:
    best = min(l[-2], l[-1])
    ans += best * (b + c)
    l[-2] -= best
    l[-1] -= best
if l[-2] > 0:
    ans += l[-2] * b
else:
    ans += l[-1] * b

print(ans)
