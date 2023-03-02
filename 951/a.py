from sys import stdin

input = stdin.readline

r = 0
b = 0
score = [10, 8, 6, 5, 4, 3, 2, 1]
scoreboard = []
place = 0
for _ in range(8):
    result = input().split()
    t = list(map(int, result[0].split(":")))
    scoreboard.append((t, result[1]))
scoreboard.sort(key=lambda x: x[0][0] * 60000 + x[0][1] * 1000 + x[0][2])
for i in scoreboard:
    if i[1] == "B":
        b += score[place]
    else:
        r += score[place]
    place += 1
print("Blue" if b > r else "Red")
