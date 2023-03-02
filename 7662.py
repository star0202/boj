from sys import stdin
from heapq import heappop, heappush

input = stdin.readline


def syncq(q):
    while q and not visited[q[0][1]]:
        heappop(q)
    return q


for _ in range(int(input())):
    t = int(input())
    visited = [False] * t
    maxq = []
    minq = []
    for i in range(t):
        op, n = input().split()
        n = int(n)
        if op == "I":
            heappush(maxq, (-n, i))
            heappush(minq, (n, i))
            visited[i] = True
        elif n == 1 and syncq(maxq):
            visited[maxq[0][1]] = False
            heappop(maxq)
        elif syncq(minq):
            visited[minq[0][1]] = False
            heappop(minq)
    if syncq(maxq) and syncq(minq):
        print(-maxq[0][0], minq[0][0])
    else:
        print("EMPTY")
