T = int(input())

for i in range(0, T):
    N = int(input())
    
    dp=[]
    for i in range(0,11):
        dp.append([])


    dp[1] = ["1"]
    dp[2] = ["2"]
    dp[3] = ["12", "21", "3"]

    for i in range(4, N+1):
        save = 0
        for j in range(1,i):

            len1 = len(dp[j])
            len2 = len(dp[i-j])

            for k in range(0,len1):
                for l in range (0, len2):
                    if(dp[j][k][-1] != dp [i-j][l][0]):
                        if(dp[i].count(dp[j][k]+dp [i-j][l]) == 0):
                            dp[i].append(dp[j][k]+dp [i-j][l])

    print(len(dp[N])%10000007)



           
        
        