dunkchi = []
count = []
for _ in range(int(input())):
    dunkchi.append(list(map(int, input().split())))
for x in dunkchi:
    cnt = 1
    for y in dunkchi:
        if x[0] < y[0] and x[1] < y[1]:
            cnt += 1
    count.append(cnt)
for x in count:
    print(x, end=" ")
