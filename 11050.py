import math

n, k = map(int, input().split())
nf = math.factorial(n)
kf = math.factorial(k)
print(nf // (kf * math.factorial(n - k)))
