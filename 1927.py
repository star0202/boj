from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

n = int(input())
heap = []

for _ in range(n):
    i = int(input())
    if i == 0:
        if not heap:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, i)