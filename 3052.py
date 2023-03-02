r = []
for x in range(0, 10):
    n = int(input())
    if not (n % 42) in r:
        r.append(n % 42)
print(len(r))
