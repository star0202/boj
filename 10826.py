n = int(input())
fn, fn1, fn2 = 0, 0, 1
if n >= 2:
    for _ in range(n):
        fn = fn1 + fn2
        fn2 = fn1
        fn1 = fn
    print(fn)
else:
    print(n)
