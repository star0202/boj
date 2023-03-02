for x in range(int(input())):
    n = list(map(int, input().split()))
    s = 0
    for y in range(n[0]):
        if n[y + 1] > (sum(n) - n[0]) / n[0]:
            s += 1
    print(f"{round(s/n[0]*100,3):.3f}%")
