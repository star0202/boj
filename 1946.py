from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    rank = sorted([list(map(int, input().split())) for _ in range(int(input()))])
    top = 0
    ans = 1
    for i in range(1, len(rank)):
        if rank[i][1] < rank[top][1]:
            top = i
            ans += 1
    print(ans)
