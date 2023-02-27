from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
coins = reversed([int(input()) for _ in range(n)])
count = 0

for x in coins:
    count += k//x
    k = k%x

print(count)