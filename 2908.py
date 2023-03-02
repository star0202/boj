a, b = map(list, input().split())
a.reverse()
b.reverse()
a = int("".join(a))
b = int("".join(b))
if a > b:
    print(a)
else:
    print(b)
