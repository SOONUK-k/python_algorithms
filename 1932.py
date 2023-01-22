size = int(input())
dp=[ 0 for _ in range(size+1)]

for i in range(size):
    tempSave = [0]+ list(map(int, input().split()))
    for j in range(1, i+2):
        tempSave[j] = max(dp[j], dp[j-1]) + tempSave[j]
    for j in range(1, i+2):
        dp[j] = tempSave[j]   
    
print(max(dp))
