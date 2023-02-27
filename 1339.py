from sys import stdin
input = stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]
word_dict = {}

for word in words:
    sqrt = len(word) - 1
    for l in word:
        if l in word_dict:
            word_dict[l] += 10 ** sqrt
        else:
            word_dict[l] = 10 ** sqrt
        sqrt -= 1
sum_list = list(word_dict.values())
sum_list.sort(reverse=True)

ans = 0
num = 9
for i in sum_list:
    ans += i * num
    num -= 1
print(ans)