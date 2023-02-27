from sys import stdin
input = stdin.readline

n = int(input())
num = [list(map(int,input().split())) for _ in range(n)]

for x in range(1, len(num)):
    num[x][0] = min(num[x-1][1], num[x-1][2]) + num[x][0]
    num[x][1] = min(num[x-1][0], num[x-1][2]) + num[x][1]
    num[x][2] = min(num[x-1][0], num[x-1][1]) + num[x][2]

print(min(num[n-1][0], num[n-1][1], num[n-1][2]))