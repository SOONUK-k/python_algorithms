N = int(input())

dp = [[0 for _ in range(3)] for _ in range(N)]
result =[[0 for _ in range(2)] for _ in range(3)]

for i in range(N):
    a, b, c = map(int, input().split())
    dp[i][0] = a
    dp[i][1] = b
    dp[i][2] = c

print (dp)
for i in range(1,N,2):
    print(dp[i][0])
    result[0][0]+=dp[i][0]
for i in range(2,N,2):
    result[0][1]+=dp[i][0]

for i in range(1,N,2):
    result[1][0]+=dp[i][1]
for i in range(2,N,2):
    result[1][1]+=dp[i][1]

for i in range(1,N,2):
    result[2][0]+=dp[i][2]
for i in range(2,N,2):
    result[2][1]+=dp[i][2]
            

print(min( dp[0][0]+min(result[1][0]+result[2][1], result[1][1]+result[2][0]), dp[0][1]+min(result[0][0]+result[2][1], result[0][1]+result[2][0])  , dp[0][2]+min(result[0][0]+result[1][1], result[0][1]+result[1][0]) ))