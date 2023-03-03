from heapq import heappop, heappush
from sys import stdin

input = stdin.readline

q = [list(map(int, input().split())) for _ in range(int(input()))]
q.sort()
room = []
heappush(room, q[0][1])
for i in range(1, len(q)):
    if q[i][0] >= room[0]:
        heappop(room)
    heappush(room, q[i][1])
print(len(room))
