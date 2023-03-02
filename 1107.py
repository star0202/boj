from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())
broken = list(map(int, input().split()))

min_cnt = abs(100 - n)
for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if int(num[j]) in broken:
            break
        elif j == len(num) - 1:
            min_cnt = min(min_cnt, abs(n - i) + len(num))
print(min_cnt)
