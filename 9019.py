# python3: TLE / pypy3: AC
from sys import stdin
from collections import deque

input = stdin.readline


def D(num):
    return (num * 2) % 10000


def S(num):
    return num - 1 if num != 0 else 9999


def L(num):
    return (num % 1000) * 10 + num // 1000


def R(num):
    return (num % 10) * 1000 + num // 10


def check_calced(num, visited, queue, cmd, cmd_old):
    calc = cmd(num)
    if calc not in visited:
        visited.add(calc)
        queue.append((calc, cmd_old + cmd.__name__))


def bfs(start, end):
    q = deque()  # 숫자, 명령어
    q.append((start, ""))
    visited = set([start])
    while q:
        num, cmd_old = q.popleft()
        if num == end:
            print(cmd_old)
            return
        for cmd in [D, S, L, R]:
            check_calced(num, visited, q, cmd, cmd_old)


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    bfs(a, b)
