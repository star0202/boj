cr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
n = input()
for x in range(8):
    if n.find(cr[x]) != -1:
        n = n.replace(cr[x], str(cr.index(cr[x])))
print(len(n))
