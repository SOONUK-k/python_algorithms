N = int(input())

dp = [[0 for _ in range(3)] for _ in range(N)]
for i in range(N):
    a, b, c = map(int, input().split())
    dp[i][0] = a
    dp[i][1] = b
    dp[i][2] = c

for i in range(0,N-1):
    dp[i+1][0] = min(dp[i][1], dp[i][2]) + dp[i+1][0]
    dp[i+1][1] = min(dp[i][0], dp[i][2]) + dp[i+1][1]
    dp[i+1][2] = min(dp[i][0], dp[i][1]) + dp[i+1][2]

print(min(dp[N-1]))
    