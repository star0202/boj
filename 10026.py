from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
arr = [list(input()) for _ in range(n)]

cnt_three = 0
cnt_two = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = True
    color = arr[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and arr[nx][ny] == color:
                dfs(nx, ny)


visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt_three += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == "G":
            arr[i][j] = "R"

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt_two += 1

print(cnt_three, cnt_two)
