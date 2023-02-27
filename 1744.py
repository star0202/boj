from sys import stdin
input = stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
p = []
n = []

for x in num:
    if x > 0:
        p.append(x)
    else:
        n.append(x)
p.sort()
n.sort(reverse=True)

r = 0
while len(p) > 1:
    a = p.pop()
    b = p.pop()
    if a == 1 or b == 1:
        r += a+b
    else:
        r += a*b
if p:
    r += p[0]

while len(n) > 1:
    a = n.pop()
    b = n.pop()
    r += a*b
if n:
    r += n[0]

print(r)