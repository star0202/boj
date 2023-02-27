from sys import stdin
import math
t = int(stdin.readline())
def prnum(x):
    if x == 1: return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True
for x in range(t):
    n = int(stdin.readline())
    a = int(n/2)
    b = int(n/2)
    for y in range(int(n/2)):
        if prnum(a) and prnum(b): print(a,b); break
        else: a -= 1; b += 1