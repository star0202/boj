n = input()
t = {3:["A","B","C"], 4:["D","E","F"], 5:["G","H","I"],6:["J","K","L"],
        7:["M","N","O"], 8:["P","Q","R","S"],9:["T","U","V"], 10:["W","X","Y","Z"]}
r = 0
for i in n:
    for k, v in t.items():
        if i in v :
            r += k
print(r)