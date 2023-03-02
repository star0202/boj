from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    cnt = 1
    q = deque([])
    q.append([x, y])
    arr[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append([nx, ny])
                cnt += 1
    return cnt


cnt = [bfs(x, y) for x in range(n) for y in range(n) if arr[x][y] == 1]
cnt.sort()
print(len(cnt))
print("\n".join(list(map(str, cnt))))
