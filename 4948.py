import math
pn = []
def prnum(x):
    if x == 1: return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True
for x in range(2,246912):
    if prnum(x): pn.append(x)
n = int(input())
while n != 0:
    c = 0
    if n == 0: break
    for x in pn:
        if n < x <= 2*n: c +=1
    print(c)
    n = int(input())