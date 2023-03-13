N = int(input())
work = [list(map(int, input().split())) for _ in range(N)]
dp=[0 for _ in range(N)]
index = [0 for _ in range(N)]

for i in range(N):
    # 범위를 넘어선 dp는 제거
    if(i+work[i][0]>N):
        dp[i]=0
        continue
    check =0
    for j in range(i):
        if(dp[j]>check and index[j] <=i):        
            check = dp[j]
            index[i] = i + work[i][0]
            dp[i] = check + work[i][1]
    
    if(check==0):
        if(i+work[i][0]<=N):
            dp[i] = work[i][1]
            index[i] = i + work[i][0]
print(max(dp))