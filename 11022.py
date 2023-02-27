time=int(input())
for x in range(0,time):
    a, b = map(int, input().split())
    print(f"Case #{x+1}: {a} + {b} = {a+b}")