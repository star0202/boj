from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

n = int(input())
deck = []
for _ in range(n):
    heappush(deck, int(input()))

if len(deck) == 1:
    print(0)
else:
    result = 0
    while len(deck) > 1:
        comp1 = heappop(deck)
        comp2 = heappop(deck)
        result += comp1+comp2
        heappush(deck, comp1+comp2)

    print(result)