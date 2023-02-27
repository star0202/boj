import sys
from collections import Counter
n = int(sys.stdin.readline())
l = []
for x in range(n):
    l.append(int(sys.stdin.readline()))
l.sort()
print(round(sum(l)/n))
print(l[n//2])
m = Counter(l).most_common()
if len(m) > 1:
    if m[0][1] == m[1][1]:
        print(m[1][0])
    else:
        print(m[0][0])
else:
    print(m[0][0])
print(l[-1]-l[0])