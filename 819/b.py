h, m = map(int, input().split(":"))
t = h * 60 + m
clock = list(map(int, input().split()))
l = int(input())


def location(time):
    if time >= 0 and time < 2 * 60:
        return 0
    elif time >= 2 * 60 and time < 4 * 60:
        return 1
    elif time >= 4 * 60 and time < 6 * 60:
        return 2
    elif time >= 6 * 60 and time < 8 * 60:
        return 3
    elif time >= 8 * 60 and time < 10 * 60:
        return 4
    else:
        return 5


for x in range(l):
    event = input().split()
    if event[1] == "^":
        try:
            clock[location(t)] = 0
        except:
            pass
    elif event[1] == "10MIN":
        t += 10
    elif event[1] == "30MIN":
        t += 30
    elif event[1] == "50MIN":
        t += 50
    elif event[1] == "2HOUR":
        t += 2 * 60
    elif event[1] == "4HOUR":
        t += 4 * 60
    elif event[1] == "9HOUR":
        t += 9 * 60
    else:
        pass
    t %= 12 * 60
if sum(clock) > 100:
    print(100)
else:
    print(sum(clock))
