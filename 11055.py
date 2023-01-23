A = int(input())
lis = list(map(int, input().split()))
savelis = [ 1 for _ in range(A)]

for i in range(A):
    tempMax=0
    tempKeep=0
    atI = lis[i]
    for j in range(i):
        if(lis[j]<atI and j<i):
            if(tempMax<savelis[j]):
                tempMax = savelis[j]
    savelis[i] = tempMax + lis[i]
    
print(max(savelis))
    

