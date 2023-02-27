t = int(input())
for x in range(t):
    k = int(input())
    n = int(input())
    a = list(range(1,n+1))
    b = a[:]
    for y in range(k):
        for i in range(n):
            if i == 0: b[0] == 1
            else:
                b[i] = sum(a[:i+1])
        a = b[:]
    print(b[len(b)-1])