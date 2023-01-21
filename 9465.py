T = int(input())
for i in range (T):
    N = int(input())
    dp1 = list(map(int, input().split()))
    dp2 = list(map(int, input().split()))
    for i in range(1,N):
        dp1[i] = max(dp1[i-1], dp2[i-1]+dp1[i])
        dp2[i] = max(dp2[i-1], dp1[i-1]+dp2[i])
    
    print(max(dp1[N-1], dp2[N-1]))
   