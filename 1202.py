from heapq import heappop, heappush
from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
jewels.sort()
bags = [int(input()) for _ in range(k)]
bags.sort()
tmp = []
ans = 0
for i in bags:
    while jewels and i >= jewels[0][0]:
        heappush(tmp, -jewels[0][1])
        heappop(jewels)
    if tmp:
        ans += -heappop(tmp)
    elif not jewels:
        break
print(ans)
