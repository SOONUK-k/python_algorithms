from itertools import combinations

N, S = map(int, input().split())
numList = list(map(int, input().split()))

output=0
for i in range(1,N+1):
    combList = combinations(numList,i)
    for j in combList:
        if sum(j) == S:
            output+=1

print(output)

