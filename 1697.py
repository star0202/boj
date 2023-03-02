from sys import stdin
from collections import deque

input = stdin.readline

MAX = 100001
arr = [0] * MAX
n, k = map(int, input().split())


def bfs(start, end):
    q = deque([start])
    while q:
        pos = q.popleft()
        if pos == end:
            return arr[pos]
        for npos in (pos - 1, pos + 1, pos * 2):
            if 0 <= npos < MAX and not arr[npos]:
                arr[npos] = arr[pos] + 1
                q.append(npos)


print(bfs(n, k))
