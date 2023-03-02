from sys import stdin

input = stdin.readline
input()
a = set(map(int, input().rstrip().split()))
b = set(map(int, input().rstrip().split()))
print(len(a ^ b))
