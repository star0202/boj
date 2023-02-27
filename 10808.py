N = input()
alphabet = list(range(97,122))

for x in alphabet:
    print(N.count(chr(x)),end = ' ')