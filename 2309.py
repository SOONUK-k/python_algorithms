from itertools import combinations

lis = []
for i in range(9):
    num = int(input())
    
    lis.append(num)
    
combi = list(combinations(lis, 7))
index =0
for i in range(len(combi)):
    if(sum(combi[i])==100):
        index = i    
        break
out = []
for i in range(7):
    out.append(combi[index][i])
out.sort()
out.reverse()
for i in range(7):
    print(out.pop())
