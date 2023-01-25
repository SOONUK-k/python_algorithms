A = int(input())
lis = list(map(int, input().split()))
result = [ 0 for _ in range(A)]

for i in range(A):
    tempMax=1001
    tempKeep=0
    atI = lis[i]
    for j in range(i):
        if(lis[j]>atI and j<i):
            if(lis[i]<lis[j] and result[j]>tempKeep):
                tempMax = lis[j]
                tempKeep=result[j]
    result[i] = tempKeep+1

print(max(result))
