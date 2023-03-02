n = int(input())
for x in range(0, n):
    r = ""
    ns, s = input().split()
    for y in range(0, len(s)):
        r += s[y] * int(ns)
    print(r)
