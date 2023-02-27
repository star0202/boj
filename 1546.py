asdf=int(input())
x = list(map(int, input().split()))
x.sort(reverse=True)
max=x[0]
qwer=0
for i in range(0,asdf):
    x[i]=x[i]/max*100
    qwer+=x[i]
print(qwer/asdf)