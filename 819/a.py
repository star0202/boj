a, b = map(int, input().split())
if a - (b*a/100) >= 100: print(0)
else: print(1)