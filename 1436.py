n = int(input())
    
def s():
    n = 1
    while True:
        if n < 100:
            n += 1
        else:
            n += 1
            if '666' in str(n - 1):
                yield n - 1                      
j = 1
for i in s():
    if j == n:
        print(i)
        break
    j += 1