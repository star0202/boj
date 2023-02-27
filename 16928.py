from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(101)]
for _ in range(n+m):
    a, b = map(int, input().split())
    arr[a] = b
visited = [False] * 101

def bfs():
    q = deque([1])
    visited[1] = True  # 방문
    while q:
        tile = q.popleft()
        for i in range(6):  # 주사위
            pos = tile + i + 1
            if pos > 100:
                continue
            cnt = arr[pos]
            if not visited[cnt]:
                visited[cnt] = visited[tile] + 1
                q.append(cnt)
                if cnt == 100:
                    return
                
bfs()
print(visited[100] - 1)