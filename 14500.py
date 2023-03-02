from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
max_val = max(map(max, arr))


def dfs(x, y, shp, tot):
    global ans
    if ans >= tot + max_val * (3 - shp):
        return
    if shp == 3:
        ans = max(ans, tot)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if shp == 1:  # ㅗ
                visited[nx][ny] = True
                dfs(x, y, shp + 1, tot + arr[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, shp + 1, tot + arr[nx][ny])
            visited[nx][ny] = False


for x in range(n):
    for y in range(m):
        visited[x][y] = True
        dfs(x, y, 0, arr[x][y])
        visited[x][y] = False

print(ans)
