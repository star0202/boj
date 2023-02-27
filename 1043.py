from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
truth = set(input().split()[1:])
party = [set(input().split()[1:]) for _ in range(m)]

for _ in range(m):
    for p in party:
        if p & truth:
            truth = truth.union(p)

result = 0
for p in party:
    if not p & truth:
        result += 1

print(result)