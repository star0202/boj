from sys import stdin
from collections import deque

input = stdin.readline

t = int(input())

for _ in range(t):
    func = input()
    n = int(input())
    if n == 0:
        input()
        arr = []
    else:
        arr = deque(input().rstrip()[1:-1].split(","))
    flag = False

    for cmd in func:
        if cmd == "R":
            flag = not flag
        elif cmd == "D":
            if len(arr) == 0:
                print("error")
                break
            else:
                if flag:
                    arr.pop()
                else:
                    arr.popleft()

    else:
        if flag:
            arr.reverse()
            print("[" + ",".join(arr) + "]")
        else:
            print("[" + ",".join(arr) + "]")
