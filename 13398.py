N = int(input())
arr = list(map(int, input().split()))

dp = [ 0 for  _ in range(N)]
dp[0] = arr[0]

for i in range(1,N):
    if(arr[i] <= arr[i]+dp[i-1]):
        dp[i] = arr[i]+dp[i-1]
    else:
        dp[i] = arr[i]

        
           
print((dp))