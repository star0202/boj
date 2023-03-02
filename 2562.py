x = []
for qwer in range(0, 9):
    x.append(int(input()))
asdf = 0
for i in range(0, len(x)):
    if asdf < x[i]:
        asdf = x[i]
print(asdf)
print(x.index(asdf) + 1)
