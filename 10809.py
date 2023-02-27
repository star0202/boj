import string
n = input()
l = list(string.ascii_lowercase)
for x in range(0, len(l)):
    print(n.find(l[x]), end = " ")