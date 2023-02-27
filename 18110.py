import sys
def round2(n):
    return int(n) + (1 if n-int(n) >= 0.5 else 0)
n = int(sys.stdin.readline().rstrip())
a = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
a.sort()
k = round2(n/20*3)
if n:
    s = sum(a[k:n-k])
    r = round2(s/(n-2*k))
else:
    r = 0
print(r)