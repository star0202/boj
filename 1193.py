from sys import stdin

n = int(stdin.readline())
k = 0
sum = 0
while n > k:
    sum += 1
    k += sum
sum += 1
if sum % 2 == 0:
    top = k - n + 1
    bottom = sum - top
else:
    bottom = k - n + 1
    top = sum - bottom

print(f"{top}/{bottom}")
