from sys import stdin

input = stdin.readline

input()

w = list(map(int, input().split()))
w.sort()
i = 1
for n in w:
    if n > i:
        break
    i += n
print(i)
