import string

a = input()
l = list(string.ascii_lowercase)
u = list(string.ascii_uppercase)
list = []
for x in range(0, len(l)):
    list.append(a.count(l[x]) + a.count(u[x]))
sl = sorted(list)
sl.sort(reverse=True)
if sl[0] == sl[1]:
    print("?")
else:
    print(chr(list.index(max(list)) + 65))
