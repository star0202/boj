n, m = map(int, input().split())
cards = list(map(int, input().split()))
i = []
for a in range(n):
    for b in range(a):
        for c in range(b):
            if cards[a] + cards[b] + cards[c] <= m:
                i.append(cards[a] + cards[b] + cards[c])
print(max(i))
