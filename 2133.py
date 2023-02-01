N = int(input())

dp = [0 for _ in range(N+1)]
dp[2] = 3
dp[4] = 11

for i in range(6, N+1, 2):
    for j in range(2, int(i/2)+1, 2):
        dp[i] += 2*(dp[j] * dp[i-j]+2)

print(dp[N])
    
