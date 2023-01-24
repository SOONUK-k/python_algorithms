A = int(input())
lis = list(map(int, input().split()))

dp1 = [0 for _ in range(A)]

for i in range(A): 
    tempKeep=0
    atI = lis[i]
    for j in range(i):
        if(lis[j]<atI and j<i):
            if(lis[i]>lis[j] and dp1[j]>tempKeep):                       
                tempKeep=dp1[j]
    dp1[i] = tempKeep+1
   
print(dp1)
result = [ 0 for _ in range(A)]

for i in range(A-1,-1,-1):
    tempKeep=0
    atI = lis[i]
    for j in range(A-1,i,-1):
        if(lis[j]<atI and result[j]>tempKeep ):
                tempKeep=result[j]
    result[i] = tempKeep+1

print(result)
dp2= [0 for _ in range (A)]

for j in range(A):
    dp2[j] = dp1[j] + result[j] -1

print(dp2)
print(max(dp2))
