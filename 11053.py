N = int(input())
el = list(map(int, input().split()))

dp =[[0 for _ in range(2)] for _ in range(N)]
#dp 에 값 저장
for i in range(N):
    dp[i][0] = el[i]




# dp[i][0]: 0엔 현재값 저장
# dp[i][1]: 길이 저장
for i in range(N):
    
    
    for j in range (i):
        if(dp[j][0]<dp[i][0] and dp[i][1] < dp[j][1]):
            dp[i][1] = dp[j][1]
    dp[i][1] +=1
          

out = [0] * N
for i in range(N):
    out[i] = dp[i][1]
print(out)
print(max(out))
