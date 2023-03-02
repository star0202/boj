from sys import stdin

input = stdin.readline
n = int(input())
r = 0
row = [0] * n


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queens(x):
    global r
    if x == n:
        r += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)


n_queens(0)
print(r)
