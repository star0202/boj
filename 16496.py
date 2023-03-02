from functools import cmp_to_key
from sys import stdin

input = stdin.readline

input()
a = input().split()
a.sort(key=cmp_to_key(lambda x, y: -1 if int(x + y) > int(y + x) else 1))
print(0 if sum(map(int, a)) == 0 else "".join(a))
