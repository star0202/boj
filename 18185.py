from sys import stdin

input = stdin.readline

n = int(input())
l = list(map(int, input().split()))
ans = 0

for x in range(n - 2):
    if l[x + 1] > l[x + 2]:  # 2개
        best = min(l[x], l[x + 1] - l[x + 2])
        ans += best * 5
        l[x] -= best
        l[x + 1] -= best
    if l[x] > 0:  # 3개
        if l[x + 1] > 0 and l[x + 2] > 0:
            best = min(l[x], l[x + 1])
            ans += best * 7
            l[x] -= best
            l[x + 1] -= best
            l[x + 2] -= best
            ans += l[x] * 3
        else:  # 1개
            ans += l[x] * 3
if l[-2] > 0 and l[-1] > 0:
    best = min(l[-2], l[-1])
    ans += best * 5
    l[-2] -= best
    l[-1] -= best
if l[-2] > 0:
    ans += l[-2] * 3
else:
    ans += l[-1] * 3

print(ans)
