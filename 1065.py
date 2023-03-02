n = int(input())
hansu = 0
for x in range(0, n):
    list = []
    for y in range(0, len(str(x + 1))):
        list.append(str(x + 1)[y])
    if len(list) < 3 or int(list[2]) - int(list[1]) == int(list[1]) - int(list[0]):
        hansu += 1
print(hansu)
