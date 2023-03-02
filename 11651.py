n = int(input())
c = []
for x in range(n):
    a, b = map(int, input().split())
    c.append([a, b])
c.sort(key=lambda x: (x[1], x[0]))
for x in c:
    print(x[0], x[1])
